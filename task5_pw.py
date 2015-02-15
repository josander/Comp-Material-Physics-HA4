#!/usr/bin/env python
from ase import *
from ase.optimize import BFGS
from ase.structure import molecule
import numpy as np
from gpaw import GPAW,Mixer
from gpaw import PW
from ase.io import write

class OccasionalWriter:
   def __init__(self):
       self.iter = 0
   def write(self):
       calc.write('CH4_SCF.%03d.gpw' % self.iter)
       self.iter += occasionally


co = molecule('CH4')
co.center(vacuum=4)

mixer=Mixer(beta=0.25, nmaxold=5, weight=50.0)
calc=GPAW(mode=PW(200), h=0.2, xc='PBE', nbands=8, mixer=mixer,txt='out_task5.txt')

occasionally = 1
calc.attach(OccasionalWriter().write, occasionally)

co.set_calculator(calc)
co.get_potential_energy()
calc.write('out_methane_v2.gpw')



