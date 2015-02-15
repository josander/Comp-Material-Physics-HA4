#!/usr/bin/env python
from ase import *
from ase.optimize import BFGS
from ase.structure import molecule
import numpy as np
from ase.parallel import rank
from gpaw import GPAW
from gpaw import PW
from gpaw import Mixer

mol = molecule('CH4')
mol.center(vacuum=4)

energycutoff=[300, 400, 500]
for ecut in energycutoff:

  mixer=Mixer(beta=0.25, nmaxold=5, weight=50.0)
  calc=GPAW(mode=PW(ecut), h=0.2, xc='PBE', mixer=mixer, nbands=8, txt='out_task3_pw_ecut'+str(ecut)+'.txt')
  mol.set_calculator(calc)
  mol.get_potential_energy()
  dyn = BFGS(mol, trajectory='mol.'+str(ecut)+'.traj',logfile='bfgs.'+str(ecut)+'.log')
  dyn.run(fmax=0.001)

# Measure O-H distance and H-O-H angle:

  pC  = mol.get_positions()[0]
  pH1 = mol.get_positions()[1]
  pH2 = mol.get_positions()[2]
  angle = np.arccos(np.dot(pH1 - pC, pH2 -pC) / 
           (np.linalg.norm(pH1-pC)*np.linalg.norm(pH2-pC)))*180.0/np.pi
    
  if rank == 0:
        print
        print '--------------------'
        print 'Cutoff energy:', ecut
        print 'C-H Distance: ', np.linalg.norm(pH1 - pC), 'Angstrom'
        print 'C-H Distance: ', np.linalg.norm(pH2 - pC), 'Angstrom'
        print 'H-C-H Angle: ', angle , 'Degrees'


