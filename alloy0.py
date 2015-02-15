#!/usr/bin/env python
import numpy as np
from ase import Atoms
from ase.io.trajectory import PickleTrajectory
from ase.optimize.bfgs import BFGS
from gpaw import GPAW
from gpaw import PW
from gpaw import FermiDirac

a = 3.210

magnesium = Atom('Mg12', 
		positions=[(0,0,0),
			   (0,0,0)],
		cell=(a,a,a))

magnesium.center()

calc=GPAW(mode=PW(200),                # Energycutoff for planewaves [eV] 
           h=0.2,                      # The distance between gridpoints AA^-1
           xc='PBE',                   # xc-functional
           nbands=8,                   # number of bands
           kpts=(2,2,2),               # number of k-points
           occupations=FermiDirac(0.1),# Fermi temperature [eV]
           txt='out_alloy0.txt')
magnesium.set_calculator(calc)

for x in np.linspace(0.95, 1.05, 7):
  magnesium.set_cell(cell * x, scale_atoms=True)
  traj.write(magnesium)




