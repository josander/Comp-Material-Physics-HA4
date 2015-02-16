#!/usr/bin/env python
import numpy as np
from ase import *
from ase.io.trajectory import PickleTrajectory
from ase.optimize.bfgs import BFGS
from gpaw import GPAW
from gpaw import PW
from gpaw import FermiDirac

#Lattice constant
a = 3.210

#Translation parameter for FCC
b = a/2

#Contruct a FCC crystal of magnesium
magnesium = Atoms('H2', positions=[(0,0,0),(0,0,b)], cell=(a,a,a))

#cell=[[0, b, b], [b, 0, b], [b, b, 0]]

magnesium.center()

calc=GPAW(mode=PW(200),                # Energycutoff for planewaves [eV] 
           h=0.2,                      # The distance between gridpoints AA^-1
           xc='PBE',                   # xc-functional
           nbands=8,                   # number of bands
           kpts=(2,2,2),               # number of k-points
           occupations=FermiDirac(0.1),# Fermi temperature [eV]
           txt='out_alloy0.txt')

magnesium.set_calculator(calc)

mg = calc.get_potential_energy()

print 'Mg energy: {0}'.format(mg)



