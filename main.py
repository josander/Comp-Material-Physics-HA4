from __future__ import print_function
from ase import Atoms
from gpaw import GPAW, PW
from gpaw.eigensolvers import Davidson
from bulkAlloy import *


"""
Main-function
"""
def main():

	# CHANGE BEFORE RUNNING THE SCRIPT
	alloyMix = 0
	struc = 'SC'
	nbrPrimCells = 4

	name = str(alloyMix)+'-'+struc
	latticeParam = 2.0  # Lattice paramter for Mg

	k = 6
	calc = GPAW(mode=PW(300),       	# cutoff
		         kpts=(k, k, k),     	# k-points
		         txt=name + '.txt',	# output file
			 eigensolver='dav') 

	while (latticeParam <= 5.5):

		# Generate bulk material
		bulk = bulkSC(alloyMix, latticeParam, 2)

		# Create calc-object
		bulk.set_calculator(calc)

		# Get potential energy
		energy = bulk.get_potential_energy()

		# Get energy per primitive cell
		energy = energy/nbrPrimCells

		# Print to output-file
		print("%f \t %f" %(energy, latticeParam))

		# New lattice parameter
		latticeParam = latticeParam + 0.1

main()
