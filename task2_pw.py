#!/usr/bin/env python
from ase import *
from ase.optimize import BFGS
from ase.structure import molecule
import numpy as np
from ase.parallel import rank
from gpaw import GPAW
from gpaw import PW
from gpaw import Mixer
import time


mol = molecule('CH4')
mol.center(vacuum=4)

mixerpara=[0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5]
for M in mixerpara:
  starttime = time.time()

  mixer=Mixer(beta=M, nmaxold=5, weight=50.0)
  calc=GPAW(mode=PW(200), h=0.2, xc='PBE', mixer=mixer, nbands=8, txt='out_task2_pw_mixer'+str(M)+'.txt')
  mol.set_calculator(calc)
  mol.get_potential_energy()
  
  endtime = time.time()
  walltime = endtime - starttime
  if rank == 0:
        print '--------------------'
        print 'Current mixing parameter:', M
        print 'Wall time:', walltime


