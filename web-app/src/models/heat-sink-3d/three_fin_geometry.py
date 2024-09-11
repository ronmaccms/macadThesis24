import torch

from sympy import Symbol, Eq, Abs, tanh

import numpy as np
from modulus.sym.utils.io import csv_to_dict
from modulus.sym.solver import Solver
from modulus.sym.geometry import Parameterization
from modulus.sym.geometry.primitives_3d import Box, Channel, Plane
from modulus.sym.key import Key
from modulus.sym.node import Node

x, y, z = Symbol("x"), Symbol("y"), Symbol("z")
x_pos = Symbol("x_pos")

fin_height_m, fin_height_s = Symbol("fin_height_m"), Symbol("fin_height_s")
fin_length_m, fin_length_s = Symbol("fin_length_m"), Symbol("fin_length_s")
fin_thickness_m, fin_thickness_s = Symbol("fin_thickness_m"), Symbol("fin_thickness_s")

fixed_param_ranges = {
    fin_height_m : 0.4,
    fin_height_s : 0.4,
    fin_length_m : 1.0,
    fin_length_s : 1.0,
    fin_thickness_m : 0.1,
    fin_thickness_s : 0.1,
}

channel_origin = (-2.5, -0.5, -0.5 )
channel_dim = (5.0, 1.0, 1.0)
heat_sink_base_origin = (-1.0, -0.5, -0.3)
heat_sink_base_dim = (1.0, 0.2, 0.6)
fin_origin = (heat_sink_base_origin[0] + 0.5 - fin_length_s / 2, -0.3, -0.3)
fin_dim = (fin_length_s, fin_height_s, fin_thickness_s)
total_fins = 2
flow_box_origin = (-1.1, -0.5, -0.5)
flow_box_dim = (1.6, 1.0, 1.0)
source_origin = (-0.7, -0.5, -0.1)
source_dim = (0.4, 0.0, 0.2)
source_area = 0.08 # source_dim [0] * source_dim[2]

class ThreeFin(object):
    def __init__(self):
        pr = Parameterization(fixed_param_ranges)
        self.pr = fixed_param_ranges

        self.channel = channel(
            channel_origin,
            (
                channel_origin[0] + channel_dim[0],
                channel_origin[1] + channel_dim[1],
                channel_origin[2] + channel_dim[2],
            ),
            parameterization = pr,
        )

        heat_sink_base = Box(
            heat_sink_base_origin,
            (
                heat_sink_base_origin[0] + heat_sink_base_dim[0],
                heat_sink_base_origin[1] + heat_sink_base_dim[1],
                heat_sink_base_origin[2] + heat_sink_base_dim[2],
            ),
            parameterization = pr,
        )

        fin_center = (
            fin_origin[0] + fin_dim[0] / 2,
            fin_origin[1] + fin_dim[1] / 2,
            fin_origin[2] + fin_dim[2] / 2,
        )

        fin = Box(
            fin_origin,
            (
                fin_origin[0] + fin_dim [0],
                fin_origin[1] + fin_dim [1],
                fin_origin[2] + fin_dim [2],
            ),
            parameterization = pr,
        )

        gap = (heat_sink_base_dim[2] - fin_dim[2]) / (total_fins - 1)
        fin_2 = fin.translate([0,0,gap])
        fin = fin + fin_2
        three_fin = heat_sink_base + fin

        center_fin_origin = (
            heat_sink_base_origin[0] + 0.5 - fin_length_m,
            fin_origin[1],
            - fin_thickness_m / 2
        )
        center_fin_dim = (fin_length_m, fin_height_m, fin_thickness_m)

        center_fin = Box(
            center_fin_origin,
            (
                center_fin_origin[0] + center_fin_dim[0],
                center_fin_origin[1] + center_fin_dim[1],
                center_fin_origin[2] + center_fin_dim[2],
            ),
            parameterization = pr,
        )

        self.three_fin = three_fin + center_fin

        self.geo = self.channel - self.three_fin

        flow_box = Box(
            flow_box_origin,
            (
                flow_box_origin[0] + flow_box_dim[0],
                flow_box_origin[1] + flow_box_dim[1],
                flow_box_origin[2] + flow_box_dim[2],
            ),
        )

        self.lr_geo = self.geo - flow_box # this is the boolean of the main cube geometry for the channel and the fins and heatsink base
        self.hr_geo = self.geo & flow_box  # this is the heat sink and fins volume area whcih is used as high res area

        lr_bounds_x = (channel_origin[0], channel_origin[0] + channel_dim[0])
        lr_bounds_y = (channel_origin[1], channel_origin[1] + channel_dim[1])
        lr_bounds_z = (channel_origin[2], channel_origin[2] + channel_dim[2])
        self.lr_bounds = {x: lr_bounds_x, y: lr_bounds_y, z: lr_bounds_z}

        hr_bounds_x = (flow_box_origin[0], flow_box_origin[0] + flow_box_dim[0])
        hr_bounds_y = (flow_box_origin[1], flow_box_origin[1] + flow_box_dim[1])
        hr_bounds_z = (flow_box_origin[2], flow_box_origin[2] + flow_box_dim[2])
        self.hr_bounds = {x: hr_bounds_x, y: hr_bounds_y, z: hr_bounds_z}

        self.inlet = Plane(
            channel_origin,
            (
                channel_origin[0],
                channel_origin[1] + channel_dim[1],
                channel_origin[2] + channel_dim[2],
            ),
            -1,
            parameterization = pr,
        )

        self.outlet = Plane(
            (channel_origin[0] + channel_dim[0],channel_origin[1], channel_origin[2]),
            (
                channel_origin[0] + channel_dim[0],
                channel_origin[1] + channel_dim[1],
                channel_origin[2] + channel_dim[2],
            ),
            1,
            parameterization = pr,
        )
        
        self.integral_plane = Plane(
            (x_pos, channel_origin[1], channel_origin[2]),
            (
                x_pos,
                channel_origin[1] + channel_dim[1],
                channel_origin[2] + channel_dim[2],
            ),
            1,
        )


