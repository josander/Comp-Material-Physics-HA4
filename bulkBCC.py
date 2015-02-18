from __future__ import print_function
from ase import Atoms
from ase.visualize import view
from gpaw import GPAW, PW
from ase.lattice.cubic import FaceCenteredCubic
from gpaw.eigensolvers import Davidson

name = '100-BCC'
a = 3.50  # Lattice paramter for Mg
nbrPrimCells = 2

k = 6
calc = GPAW(mode=PW(300),       # cutoff
            kpts=(k, k, k),     # k-points
            txt=name + '.txt',	# output file
	    eigensolver='dav') 

while (a <= 5.5):
	b = a / 2

	bulk = Atoms(['Al','Al','Al','Al'], 
		     positions=[(0,0,0),
				(a,0,0),
				(b,b,b),
				(a+b,b,b)],
	             cell=[2*a, a, a],
	             pbc=True)



	bulk.set_calculator(calc)

	energy = bulk.get_potential_energy()

	energy = energy/nbrPrimCells

	calc.write(name + '.gpw')
	print("%f \t %f" %(energy, a))

	a = a + 0.1
