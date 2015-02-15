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

calc=GPAW(mode=PW(400),                 # Energycutoff for planewaves [eV] 
           basis='dzp',
           h=0.2,                       # The distance between gridpoints AA^-1
           xc='PBE',                    # xc-functional
           nbands=20,                   # number of bands
           kpts=(12,12,12),             # number of k-points
           occupations=FermiDirac(0.1), # Fermi temperature [eV]
           txt='out_task7_Sibulk.txt')
silicon.set_calculator(calc)
silicon.get_potential_energy()

calc.write('silicon.gpw', mode='all')



