from __future__ import print_function
from ase import Atoms
from ase.visualize import view
from gpaw import GPAW, PW
from ase.lattice.cubic import FaceCenteredCubic
from gpaw.eigensolvers import Davidson

name = 'Al-SC'
a = 4.05  # Lattice paramter for Mg
b = a / 2

bulk = Atoms('Al', 
	     positions=[(0,0,0)],
             cell=[b, b, b],
             pbc=True)

k = 8
calc = GPAW(mode=PW(500),       # cutoff
            kpts=(k, k, k),     # k-points
            txt=name + '.txt',	# output file
	    eigensolver='dav') #lol  

bulk.set_calculator(calc)

energy = bulk.get_potential_energy()
calc.write(name + '.gpw')
print('Energy:', energy, 'eV')
