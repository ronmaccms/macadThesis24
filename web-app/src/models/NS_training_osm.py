from wakepy import keep
import os
import warnings

import torch
import numpy as np

from sympy import Symbol, Eq

import modulus.sym
from modulus.sym.hydra import to_absolute_path, instantiate_arch, ModulusConfig
from modulus.sym.solver import Solver
from modulus.sym.domain import Domain
from modulus.sym.geometry.primitives_2d import Rectangle, Line, Channel2D, Polygon
from modulus.sym.utils.sympy.functions import parabola
from modulus.sym.utils.io import csv_to_dict

# EQUATIONS
from modulus.sym.eq.pdes.navier_stokes import NavierStokes, GradNormal
from modulus.sym.eq.pdes.basic import NormalDotVec
from modulus.sym.eq.pdes.turbulence_zero_eq import ZeroEquation
from modulus.sym.eq.pdes.advection_diffusion import AdvectionDiffusion

from modulus.sym.domain.constraint import (
    PointwiseBoundaryConstraint,
    PointwiseInteriorConstraint,
    IntegralBoundaryConstraint,
)

from modulus.sym.domain.monitor import PointwiseMonitor
from modulus.sym.domain.validator import PointwiseValidator

from modulus.sym.key import Key
from modulus.sym.node import Node
from modulus.sym.geometry import Parameterization, Parameter

import matplotlib.pyplot as plt
from shapely.geometry import Polygon as ShapelyPolygon
import matplotlib.patches as patches

# Import helper functions
from helpers import (
    fetch_building_footprints, 
    extract_rectangle_points, 
    plot_rectangle_points, 
    calculate_min_max_coordinates,
    calculate_combined_boundary  # Use this version without the expansion_factor argument
)

@modulus.sym.main(config_path="./", config_name="config.yaml")
def run(cfg: ModulusConfig) -> None:
    
    # Fetch the building footprints
    location_point = (40.748817, -73.985428)  # Times Square, NYC
    radius = 100  # Radius in meters
    simrec_list, minun_rectangle_all = fetch_building_footprints(location_point, radius)
    
    # Extract rectangle points for all building footprints
    rectangle_points_list = extract_rectangle_points(simrec_list)

    # Scale the geometry if necessary (modify the scaling factor as needed)
    scaling_factor = 10  # Example scaling factor
    cleaned_rectangle_points_list = [
        [(x * scaling_factor, y * scaling_factor) for x, y in points]
        for points in rectangle_points_list
    ]

    # Remove the last repeated point from each building’s points to get only 4 points per building
    cleaned_rectangle_points_list = [points[:-1] for points in cleaned_rectangle_points_list]

    # Plot all building footprints with corner points
    plot_rectangle_points(cleaned_rectangle_points_list, boundary_rectangle=None)

    # Calculate the minimum and maximum coordinates across all footprints
    min_x, max_x, min_y, max_y = calculate_min_max_coordinates(cleaned_rectangle_points_list)
    
    # Calculate the channel dimensions based on all building footprints
    channel_length, channel_width = calculate_combined_boundary(cleaned_rectangle_points_list)

    # Plot the combined minimum rotated rectangle around all building footprints
    plot_rectangle_points(cleaned_rectangle_points_list, boundary_rectangle=(min_x, min_y, max_x, max_y))

    # Create Modulus Polygon objects for each building footprint using tuple lists
    modulus_polygons = [Polygon(points) for points in cleaned_rectangle_points_list]

    # Start with the full channel
    channel = Channel2D(
        (channel_length[0], channel_width[0]), (channel_length[1], channel_width[1])
    )

    # Subtract each building footprint from the channel to create the final geometry
    geo = channel
    for i, poly in enumerate(modulus_polygons):
        geo = geo - poly
        print(f"Subtracted geometry {i+1}")
        
        # Debug plot to verify subtraction
        fig, ax = plt.subplots(figsize=(7, 5))
        # Plot the channel boundary after subtraction
        channel_polygon = ShapelyPolygon([(channel_length[0], channel_width[0]), (channel_length[0], channel_width[1]),
                                          (channel_length[1], channel_width[1]), (channel_length[1], channel_width[0])])
        patch = patches.Polygon(list(channel_polygon.exterior.coords), closed=True, fill=None, edgecolor='blue', linewidth=2)
        ax.add_patch(patch)

        # Plot the subtracted polygon
        building_polygon = ShapelyPolygon(cleaned_rectangle_points_list[i])
        patch = patches.Polygon(list(building_polygon.exterior.coords), closed=True, fill=None, edgecolor='red', linewidth=2)
        ax.add_patch(patch)

        ax.set_xlim([min_x - 10, max_x + 10])
        ax.set_ylim([min_y - 10, max_y + 10])
        ax.set_xlabel('X Coordinate')
        ax.set_ylabel('Y Coordinate')
        ax.set_title(f'Debug Plot: Geometry {i+1} Subtraction')
        plt.show()

    # Print to verify
    print("Final Geometry Created.")

    # Parametrically define the heat sink wall polygon
    heat_sink_x_start = channel_length[1] - 0.1 * (channel_length[1] - channel_length[0])  # 10% from the end of the channel
    heat_sink_x_end = channel_length[1]  # At the end of the channel
    heat_sink_y_start = channel_width[0]  # Full height of the channel
    heat_sink_y_end = channel_width[1]

    heat_sink_polygon = ShapelyPolygon([
        (heat_sink_x_start, heat_sink_y_start),
        (heat_sink_x_end, heat_sink_y_start),
        (heat_sink_x_end, heat_sink_y_end),
        (heat_sink_x_start, heat_sink_y_end)
    ])

    # Plot the combined geometry with heat sink boundary
    fig, ax = plt.subplots(figsize=(7, 5))

    # Plot the channel boundary
    channel_polygon = ShapelyPolygon([(channel_length[0], channel_width[0]), (channel_length[0], channel_width[1]),
                                    (channel_length[1], channel_width[1]), (channel_length[1], channel_width[0])])
    patch = patches.Polygon(list(channel_polygon.exterior.coords), closed=True, fill=None, edgecolor='blue', linewidth=2)
    ax.add_patch(patch)

    # Plot each building footprint
    for points in cleaned_rectangle_points_list:
        building_polygon = ShapelyPolygon(points)
        patch = patches.Polygon(list(building_polygon.exterior.coords), closed=True, fill=None, edgecolor='red', linewidth=2)
        ax.add_patch(patch)

    # Highlight the heat sink wall
    patch = patches.Polygon(list(heat_sink_polygon.exterior.coords), closed=True, fill=None, edgecolor='green', linewidth=2)
    ax.add_patch(patch)

    # Set plot limits and labels
    ax.set_xlim([min_x - 10, max_x + 10])
    ax.set_ylim([min_y - 10, max_y + 10])
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_title(f'Geometry with Heat Sink Wall Highlighted')
    plt.show()

    # Define the inlet and outlet
    inlet_line = Line(
        (channel_length[0], channel_width[0]),
        (channel_length[0], channel_width[1]), -1
    )
    outlet_line = Line(
        (channel_length[1], channel_width[0]),
        (channel_length[1], channel_width[1]), 1
    )
    
    x_pos = Parameter("x_pos")

    integral_line = Line(
        (x_pos, channel_width[0]),
        (x_pos, channel_width[1]),
        1,
        parameterization=Parameterization({x_pos: channel_length}),
    )
    
    nu = 0.01  # Viscosity
    diffusivity = nu / 5  # Diffusivity
    inlet_vel = 1.5  # Inlet velocity
    heat_sink_temp = 350  # Temperature of the heat sink
    base_temp = 293.498  # Base temperature
    temp_diff = (heat_sink_temp - base_temp) / 273.15
    print(f"Temperature difference applied at heat sink wall: {temp_diff}")

    
    ze = ZeroEquation(
        nu=nu, rho=1.0, dim=2, max_distance=(channel_width[1] - channel_width[0]) / 2
    )

    ns = NavierStokes(nu=ze.equations["nu"], rho=1.0, dim=2, time=False)

    ade = AdvectionDiffusion(T="c", rho=1.0, D=diffusivity, dim=2, time=False)
    gn_c = GradNormal("c", dim=2, time=False)
    normal_dot_vet = NormalDotVec(["u", "v"])
    
    flow_net = instantiate_arch(
        input_keys=[Key("x"), Key("y")],
        output_keys=[Key("u"), Key("v"), "p"],
        cfg=cfg.arch.fully_connected,
    )

    heat_net = instantiate_arch(
        input_keys=[Key("x"), Key("y")],
        output_keys=[Key("c")],
        cfg=cfg.arch.fully_connected,
    )

    nodes = (
        ns.make_nodes()
        + ze.make_nodes()
        + ade.make_nodes(detach_names=["u", "v"])
        + gn_c.make_nodes()
        + normal_dot_vet.make_nodes()
        + [flow_net.make_node(name="flow_network")]
        + [heat_net.make_node(name="heat_network")]
    )

    domain = Domain()

    # Add boundary conditions
    y = Symbol("y")  # Make sure y is defined
    inlet_parabola = parabola(
        y, inter_1=channel_width[0], inter_2=channel_width[1], height=inlet_vel
    )

    inlet = PointwiseBoundaryConstraint(
        nodes=nodes,
        geometry=inlet_line,
        outvar={"u": inlet_parabola, "v": 0, "c": 0},
        batch_size=cfg.batch_size.inlet,
    )
    domain.add_constraint(inlet, "inlet")

    outlet = PointwiseBoundaryConstraint(
        nodes=nodes,
        geometry=outlet_line,
        outvar={"p": 0},
        batch_size=cfg.batch_size.outlet,
    )
    domain.add_constraint(outlet, "outlet")

    hs_wall = PointwiseBoundaryConstraint(
        nodes=nodes,
        geometry=geo,  # Now the full geometry including all subtracted polygons
        outvar={"u": 0, "v": 0, "c": temp_diff},
        # outvar={"u": 0, "v": 0, "c": (heat_sink_temp - base_temp) / 273.15},
        batch_size=cfg.batch_size.hs_wall,
    )
    domain.add_constraint(hs_wall, "heat_sink_wall")

    channel_wall = PointwiseBoundaryConstraint(
        nodes=nodes,
        geometry=channel,  # Use the original channel for this boundary condition
        outvar={"u": 0, "v": 0, "normal_gradient_c": 0},
        batch_size=cfg.batch_size.channel_wall,
    )
    domain.add_constraint(channel_wall, "channel_wall")

    interior_flow = PointwiseInteriorConstraint(
        nodes=nodes,
        geometry=geo,
        outvar={"continuity": 0, "momentum_x": 0, "momentum_y": 0},
        batch_size=cfg.batch_size.interior_flow,  # Increase this value if needed
        compute_sdf_derivatives=True,
        lambda_weighting={
            "continuity": Symbol("sdf"),
            "momentum_x": Symbol("sdf"),
            "momentum_y": Symbol("sdf"),
        }
    )
    domain.add_constraint(interior_flow, "interior_flow")

    interior_heat = PointwiseInteriorConstraint(
        nodes=nodes,
        geometry=geo,
        outvar={"advection_diffusion_c": 0},
        batch_size=cfg.batch_size.interior_heat,  # Increase this value if needed
        lambda_weighting={"advection_diffusion_c": 1},
    )
    domain.add_constraint(interior_heat, "interior_heat")

    # Integration periodical 
    def integral_criteria(invar, params):
        sdf = geo.sdf(invar, params)
        return np.greater(sdf["sdf"], 0)
    
    integral_continuity = IntegralBoundaryConstraint(
        nodes=nodes,
        geometry=integral_line,
        outvar={"normal_dot_vel": 1},
        batch_size=cfg.batch_size.num_integral_continuity,
        integral_batch_size=cfg.batch_size.integral_continuity,
        lambda_weighting={"normal_dot_vel": 0.1},
        criteria=integral_criteria,
    )
    domain.add_constraint(integral_continuity, "integral_continuity")

    # Add monitors
    force = PointwiseMonitor(
        geo.sample_boundary(100),
        output_names=["p"],
        metrics={
            "force_x": lambda var: torch.sum(var["normal_x"] * var["area"] * var["p"]),
            "force_y": lambda var: torch.sum(var["normal_y"] * var["area"] * var["p"]),
        },
        nodes=nodes,
    )
    domain.add_monitor(force)

    print("Checking heat sink wall constraint:")
    print(f"Boundary geometry: {geo.bounds}")
    print(f"Applied boundary condition: u=0, v=0, c={temp_diff}")


    # Print important parameters to verify they are correctly set
    print(f"nu: {nu}, inlet_vel: {inlet_vel}, diffusivity: {diffusivity}")
    print(f"Channel Length: {channel_length}, Channel Width: {channel_width}")
    # Confirm boundary conditions and domain setup
    print(f"Inlet parabola: {inlet_parabola}")
    print(f"Domain Constraints: {domain.constraints}")

    # Solver initialization and solve
    slv = Solver(cfg, domain)
    slv.solve()

if __name__ == "__main__":
    run()
