"""Bulk Al(fcc) test"""
from __future__ import print_function
from ase import Atoms
from ase.visualize import view
from gpaw import GPAW, PW
from ase.lattice.cubic import FaceCenteredCubic
from gpaw.eigensolvers import Davidson

name = 'Al-fcc'
a = 4.05  # fcc lattice paramter
b = a / 2

#bulk = Atoms('Mg',
#             cell=[[b, 0, 0],
#                   [0, b, 0],
#                   [0, 0, b]],
#             pbc=True)

bulk = FaceCenteredCubic(directions=[[1,0,0], [0,1,0], [0,0,1]],
                          size=(1,1,1), symbol='Al', pbc=(1,1,1))

#view(bulk)

k = 8
calc = GPAW(mode=PW(500),       # cutoff
            #kpts=(k, k, k),     # k-points
            txt=name + '.txt',	# output file
	    eigensolver=Davidson()) #lol  

bulk.set_calculator(calc)

energy = bulk.get_potential_energy()
calc.write(name + '.gpw')
print('Energy:', energy, 'eV')
