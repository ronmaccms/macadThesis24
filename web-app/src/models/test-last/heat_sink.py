import os
import warnings

import torch
import numpy as np

from sympy import Symbol, Eq

import modulus.sym
from modulus.sym.hydra import to_absolute_path, instantiate_arch, ModulusConfig
from modulus.sym.solver import Solver
from modulus.sym.domain import Domain
from modulus.sym.geometry.primitives_2d import Rectangle, Polygon, Line, Channel2D
from modulus.sym.utils.sympy.functions import parabola # for the input flow 
from modulus.sym.utils.io import csv_to_dict

#equations
from modulus.sym.eq.pdes.navier_stokes import NavierStokes, GradNormal # grad normal would calculate the gradient and the walls to make sure the flow is zero
from modulus.sym.eq.pdes.advection_diffusion import AdvectionDiffusion # 
from modulus.sym.eq.pdes.basic import NormalDotVec # the direction of flow
from modulus.sym.eq.pdes.turbulence_zero_eq import ZeroEquation

from modulus.sym.domain.constraint import(
    PointwiseBoundaryConstraint,
    IntegralBoundaryConstraint,
    PointwiseInteriorConstraint,
)

from modulus.sym.domain.monitor import PointwiseMonitor
from modulus.sym.domain.validator import PointwiseValidator

from modulus.sym.key import Key
from modulus.sym.node import Node # based on the equation and boundary condition the nodes will represent and show the directions and movement
from modulus.sym.geometry import Parameterization, Parameter

@modulus.sym.main(config_path="./", config_name="config.yaml")
def run(cfg: ModulusConfig) -> None :
    channel_lenght = (-2.5, 2.5)
    channel_width = (-0.5, 0.5)
    heat_sink_origin = (-1, -0.3)
    nr_heat_sink_fins = 3
    gap = 0.15+0.1
    heat_sink_length = 1.0
    heat_sink_fin_thickness = 0.1
    inlet_vel = 1.5
    heat_sink_temp = 350
    base_temp = 293.498
    nu = 0.01 # viscozity
    diffusivity = 0.01/5

    x, y = Symbol("x"), Symbol("y")

    channel = Channel2D(
        (channel_lenght[0], channel_width[0]), (channel_lenght[0], channel_width[0])
    )

    heat_sink = Rectangle(
        heat_sink_origin,
        (heat_sink_origin[0]+heat_sink_length),
        (heat_sink_origin[0]+heat_sink_fin_thickness),
    )

    if __name__ == "__main__":
        run()