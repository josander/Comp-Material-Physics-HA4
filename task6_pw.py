#!/usr/bin/env python
import numpy as np
from ase import Atoms
from ase.structure import bulk
from ase.io.trajectory import PickleTrajectory
from ase.optimize.bfgs import BFGS
from gpaw import GPAW
from gpaw import PW
from gpaw import FermiDirac

silicon = bulk('Si', 'diamond', a=5.459)
cell = silicon.get_cell()
traj = PickleTrajectory('silicon.traj', 'w')

calc=GPAW(mode=PW(200),                # Energycutoff for planewaves [eV] 
           h=0.2,                      # The distance between gridpoints AA^-1
           xc='PBE',                   # xc-functional
           nbands=8,                   # number of bands
           kpts=(2,2,2),               # number of k-points
           occupations=FermiDirac(0.1),# Fermi temperature [eV]
           txt='out_task6_Sibulk.txt')
silicon.set_calculator(calc)
for x in np.linspace(0.95, 1.05, 7):
  silicon.set_cell(cell * x, scale_atoms=True)
  traj.write(silicon)




