from __future__ import print_function
from ase import Atoms
from ase.visualize import view
from gpaw import GPAW, PW
from ase.lattice.cubic import FaceCenteredCubic
from gpaw.eigensolvers import Davidson

name = '100-SC'
a = 4.00  # Lattice paramter for Mg
nbrPrimCells = 4

k = 6
calc = GPAW(mode=PW(300),       # cutoff
	         kpts=(k, k, k),     # k-points
	         txt=name + '.txt',	# output file
		 eigensolver='dav') 


while (a <= 5.0):

	bulk = Atoms(['Al','Al','Al','Al'], 
		     positions=[(0,0,0),
				(a,a,0),
				(0,0,a),
				(a,a,a)],
	             cell=[2*a, a, 2*a],
	             pbc=True)

	bulk.set_calculator(calc)

	energy = bulk.get_potential_energy()

	energy = energy/nbrPrimCells

	calc.write(name + '.gpw')
	print("%f \t %f" %(energy, a))

	a = a + 0.1
