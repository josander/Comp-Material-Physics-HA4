from __future__ import print_function
from ase import Atoms
from gpaw import GPAW, PW
from gpaw.eigensolvers import Davidson
from bulkAlloy import *


"""
Main-function
"""
def main():
	alloyMix = 75
	latticeParam = 4

	bulk = bulkSC(alloyMix, latticeParam, 2)
	test = bulk.get_atomic_numbers()
	
	print(test)
	
"""
	# Parameters for the calculator
	name = 'bulkSC0'
	k = 8
	calc = GPAW(mode=PW(200),       # cutoff
	           kpts=(k, k, k),     	# k-points
	            txt=name + '.txt',	# output file
		    eigensolver='dav') 

	latticeParam = 4.0
	nbrPrimCells = 4

	while (latticeParam < 5.0):

		# Generate different type of bulk systems
		sc0 = bulkSC(0, latticeParam, 2)

		# Get the energy and save output
		sc0.set_calculator(calc)
		energy = sc0.get_potential_energy()

		# Divide the energy with number of primitive cells in the supercell
		energy = energy/nbrPrimCells
		calc.write(name + '.gpw')
		print('Energy:', energy, 'eV')

		# New lattice parameter
		latticeParam = latticeParam + 0.5
"""

main()
