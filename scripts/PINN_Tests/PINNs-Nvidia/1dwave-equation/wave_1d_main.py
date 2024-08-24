import numpy as np
from sympy import Symbol, sin

import modulus.sym

from modulus.sym.hydra import instantiate_arch, ModulusConfig
from modulus.sym.solver import Solver 
from modulus.sym.domain import Domain
from modulus.sym.geometry.primitives_1d import Line1D
from modulus.sym.domain.constraint import PointwiseBoundaryConstraint, PointwiseInteriorConstraint

from modulus.sym.domain.validator import PointwiseValidator
from modulus.sym.key import Key
from modulus.sym.node import Node

from wave_equation_main import WaveEquation1D

@modulus.sym.main(config_path="./", config_name= "config_main.yml")

def run(cfg: ModulusConfig) -> None:
    we = WaveEquation1D(c=1.0)
    
    wave_net = instantiate_arch(
        input_keys=[Key("x"), Key("t")],
        output_keys=[Key("u")],
        cfg=cfg.arch.fully_connected,
    )
    nodes = we.make_nodes() + [wave_net.make_node(name="wave_network")]
    
    x_symbol, t_symbol = Symbol("x"), Symbol("t")
    L = float(np.pi)
    geo = Line1D(0,L)
    time_range = {t_symbol: (0,2*L)}
    
    domain = Domain()
    
    IC = PointwiseInteriorConstraint(
        nodes = nodes,
        geometry = geo,
        outvar = {"u": sin(x_symbol), "u__t" : sin(x_symbol)},
        batch_size = cfg.batch_size.IC,
        lambda_weighting = {"u":1.0, "u__t":1.0},
        parameterization = {t_symbol: 0.0},
    )
    domain.add_constraint(IC, "IC")
    
    BC = PointwiseBoundaryConstraint(
        nodes = nodes,
        geometry = geo,
        outvar = {"u": 0},
        batch_size = cfg.batch_size.BC,
        parameterization = time_range,
    )
    domain.add_constraint(BC, "BC")
    
    interior = PointwiseInteriorConstraint(
        nodes = nodes,
        geometry = geo,
        outvar = {"wave_equation": 0},
        batch_size = cfg.batch_size.interior,
        parameterization = time_range,
    )
    domain.add_constraint(interior, "interior")
    
    deltaT = 0.01
    deltaX = 0.01
    x = np.arange(0,L, deltaX)
    t = np.arange(0,2*L, deltaT)
    X,T = np.meshgrid(x,t)
    X = np.expand_dims(X.flatten(), axis = -1)
    T = np.expand_dims(T.flatten(), axis = -1)
    u = np.sin(X) * (np.cos(T) + np.sin(T))
    
    invar_numpy = {"x": X, "t":T}
    outvar_numpy = {"u": u}
    validator = PointwiseValidator (
        nodes = nodes, invar = invar_numpy, true_outvar = outvar_numpy, batch_size = 128
    )
    domain.add_validator(validator)
    
    slv = Solver(cfg, domain)
    
    slv.solve()


if __name__ =="__main__":
    run()