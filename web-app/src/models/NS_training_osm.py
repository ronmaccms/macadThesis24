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
from modulus.sym.geometry.primitives_2d import Rectangle, Line, Channel2D
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
from modulus.sym.geometry.primitives_2d import Polygon

import matplotlib.pyplot as plt
from shapely.geometry import Polygon as ShapelyPolygon
import matplotlib.patches as patches
from osm import (
        fetch_building_footprints, 
        plot_rectangle_points, 
        extract_rectangle_points, 
        calculate_combined_boundary, 
        calculate_length_and_width, 
        update_channel_dimensions,
        calculate_min_max_coordinates,
)

@modulus.sym.main(config_path="./", config_name="config.yaml")
def run(cfg: ModulusConfig) -> None :
        
        location_point = (40.748817, -73.985428)  # Times Square, NYC
        radius = 100  # Radius in meters
        simrec_list, minun_rectangle_all  = fetch_building_footprints(location_point, radius)
        rectangle_points_list = extract_rectangle_points(simrec_list)
        min_recall = [minun_rectangle_all]

        # Print the corner points and remove the last point (closing point)
        for i, rect_points in enumerate(rectangle_points_list):
            # Remove the last item (closing point) from the list of corners
            rect_points.pop()  # Remove last point
            length, width = calculate_length_and_width(rect_points)
            print(f"Rectangle {i+1}: Length = {length}, Width = {width}")

        # channel_length, channel_width = update_channel_dimensions(rectangle_points_list)
        min_x, max_x, min_y, max_y = calculate_min_max_coordinates(rectangle_points_list)

        # Calculated based on channel dimensions
        heat_sink_origin = (min_x + 0.1 * (max_x - min_x), min_y + 0.1 * (max_y - min_y))
        nr_heat_sink_fins = len(simrec_list)
        heat_sink_length = 0.2 * (max_x - min_x)  # For example, 20% of the channel's length
        heat_sink_fin_thickness = 0.05 * (max_y - min_y)  # For example, 5% of the channel's width
        gap = 0.1 * (max_y - min_y)  # 10% of the channel's width

        # other parameters
        inlet_vel = 1.5
        heat_sink_temp = 350
        base_temp = 293.498
        nu = 0.01
        diffusivity = 0.01/5

        # Use the calculated channel length and width
        channel_length = (min_x, max_x)
        channel_width = (min_y, max_y)

        # Plot the original rectangles using simrec_list
        plot_rectangle_points(simrec_list)
        # Additionally, plot the combined minimum rotated rectangle
        plot_rectangle_points(min_recall)

        x, y = Symbol("x"), Symbol("y")

        channel = Channel2D(
            (channel_length[0],channel_width[0]),(channel_length[1],channel_width[1])
        )

        heat_sink = Rectangle(
            heat_sink_origin,
            (
                (heat_sink_origin[0]+heat_sink_length),
                (heat_sink_origin[1]+heat_sink_fin_thickness),
            ),
        )

        for i in range(1, nr_heat_sink_fins):
            heat_sink_origin = (heat_sink_origin[0], heat_sink_origin[1]+gap)
            fin = Rectangle(
                heat_sink_origin,
                (
                    heat_sink_origin[0] + heat_sink_length,
                    heat_sink_origin[1] + heat_sink_fin_thickness,
                ),
            )

            heat_sink = heat_sink + fin 

        geo = channel - heat_sink

        inlet = Line(
            (channel_length[0], channel_width[0]),
            (channel_length[0], channel_width[1]), -1
            )
        outlet = Line(
            (channel_length[1], channel_width[0]),
            (channel_length[1], channel_width[1]), 1
            )
        
        x_pos = Parameter("x_pos")

        integral_line = Line(
            (x_pos, channel_width[0]),
            (x_pos, channel_width[1]),
            1,
            parameterization = Parameterization({x_pos:channel_length}),
        )
        
        ze = ZeroEquation(
            nu = nu, rho = 1.0, dim = 2, max_distance = (channel_width[1]-channel_width[0])/2
        )

        ns = NavierStokes(nu = ze.equations["nu"], rho = 1.0, dim = 2, time = False)

        ade = AdvectionDiffusion(T = "c", rho = 1.0, D = diffusivity, dim = 2, time = False)
        gn_c = GradNormal("c", dim = 2, time = False)    
        # when we calculate te surface we also need to calculate the dot product of the surface as it solves
        normal_dot_vet = NormalDotVec(["u", "v"])
        
        flow_net = instantiate_arch(
            input_keys = [Key("x"), Key("y")],
            output_keys = [Key("u"), Key("v"), Key("p")],
            cfg = cfg.arch.fully_connected,
        )

        heat_net = instantiate_arch(
            input_keys = [Key("x"), Key("y")],
            output_keys = [Key("c")],
            cfg = cfg.arch.fully_connected,
        )

        nodes = (
            ns.make_nodes()
            +ze.make_nodes()
            +ade.make_nodes(detach_names=["u", "v"])
            +gn_c.make_nodes()
            +normal_dot_vet.make_nodes()
            + [flow_net.make_node(name="flow_network")]
            + [heat_net.make_node(name="heat_network")]
        )

        domain = Domain()

        # add boundary conditions
        inlet_parabola = parabola(
            y, inter_1=channel_width[0], inter_2=channel_width[1], height=inlet_vel
        )

        inlet = PointwiseBoundaryConstraint(
            nodes = nodes,
            geometry = inlet,
            outvar = {"u": inlet_parabola, "v": 0, "c": 0},
            batch_size = cfg.batch_size.inlet,
        )
        domain.add_constraint(inlet, "inlet")

        outlet = PointwiseBoundaryConstraint(
            nodes = nodes,
            geometry = outlet,
            outvar = {"p": 0},
            batch_size = cfg.batch_size.outlet,
        )
        domain.add_constraint(outlet, "outlet")

        hs_wall = PointwiseBoundaryConstraint(
            nodes = nodes,
            geometry = heat_sink,
            outvar = {"u": 0,"v": 0,"c": (heat_sink_temp-base_temp)/273.15},
            batch_size = cfg.batch_size.hs_wall,
        )
        domain.add_constraint(hs_wall, "heat_sink_wall")

        channel_wall = PointwiseBoundaryConstraint(
            nodes = nodes,
            geometry = channel,
            outvar = {"u": 0, "v": 0, "normal_gradient_c": 0},
            batch_size = cfg.batch_size.channel_wall,
        )
        domain.add_constraint(channel_wall, "channel_wall")

        interior_flow = PointwiseInteriorConstraint(
            nodes = nodes,
            geometry = geo,
            outvar = {"continuity": 0, "momentum_x": 0, "momentum_y": 0},
            batch_size = cfg.batch_size.interior_flow,
            compute_sdf_derivatives = True,
            lambda_weighting = {
                "continuity": Symbol("sdf"),
                "momentum_x": Symbol("sdf"),
                "momentum_y": Symbol("sdf"),
            }
        )
        domain.add_constraint(interior_flow, "interior_flow")

        interior_heat = PointwiseInteriorConstraint(
            nodes = nodes,
            geometry = geo,
            outvar = {"advection_diffusion_c": 0},
            batch_size = cfg.batch_size.interior_heat,
            lambda_weighting = {"advection_diffusion_c": 1},
        )
        domain.add_constraint(interior_heat, "interior_heat")

        # integration periodical 
        def integral_criteria(invar, params):
            sdf = geo.sdf(invar, params)
            return np.greater(sdf["sdf"], 0)
        
        integral_continuity = IntegralBoundaryConstraint(
            nodes = nodes,
            geometry = integral_line,
            outvar = {"normal_dot_vel": 1},
            batch_size = cfg.batch_size.num_integral_continuity,
            integral_batch_size = cfg.batch_size.integral_continuity,
            lambda_weighting = {"normal_dot_vel": 0.1},
            criteria = integral_criteria,
        )
        domain.add_constraint(integral_continuity, "integral_continuity")

        # add monitors
        force = PointwiseMonitor(
            heat_sink.sample_boundary(100),
            output_names=["p"],
            metrics = {
                "force_x": lambda var: torch.sum(var["normal_x"] * var["area"] * var["p"]),
                "force_y": lambda var: torch.sum(var["normal_y"] * var["area"] * var["p"]),
            },
            nodes = nodes,
        )
        domain.add_monitor(force)

        slv = Solver(cfg, domain)

        slv.solve()

if __name__ == "__main__":
    run()