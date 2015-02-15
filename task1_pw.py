#!/usr/bin/env python
from ase import *
from ase.optimize import BFGS
from ase.structure import molecule
import numpy as np
from gpaw import GPAW
from gpaw import PW

mol = molecule('CH4')
mol.center(vacuum=4)

calc=GPAW(mode=PW(200), h=0.2, xc='PBE', nbands=8, txt='out_task1_pw.txt')
mol.set_calculator(calc)

dyn = BFGS(mol, trajectory='mol_task1_pw.traj',logfile='bfgs_task1_pw.log')
dyn.run(fmax=0.001)

calc.write('out_methane.gpw')

