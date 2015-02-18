from __future__ import print_function
from ase import Atoms
from ase.visualize import view
from gpaw import GPAW, PW
from ase.lattice.cubic import FaceCenteredCubic
from gpaw.eigensolvers import Davidson

name = '100-FCC'
a = 3.50

k = 6
calc = GPAW(mode=PW(300),       # cutoff
	         kpts=(k, k, k),     # k-points
	         txt=name + '.txt',	# output file
		 eigensolver='dav') 

while (a <= 5.5):
	b = a / 2

	bulk = Atoms(['Al','Al','Al','Al'], 
		     positions=[(0,0,0),
				(b,b,0),
				(0,b,b),
				(b,0,b)],
	             cell=[a, a, a],
	             pbc=True)

	bulk.set_calculator(calc)

	energy = bulk.get_potential_energy()

	calc.write(name + '.gpw')
	print("%f \t %f" %(energy, a))

	a = a + 0.1
