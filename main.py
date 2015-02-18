from __future__ import print_function
from ase import Atoms
from gpaw import GPAW, PW
from gpaw.eigensolvers import Davidson
from bulkAlloy import *


"""
Main-function
"""
def main():

	# Change these before running the script
	alloyMix = 75
	struc = 'SC'
	nbrPrimCells = 4

	name = str(alloyMix)+'-'+struc
	latticeParam = 3.50  # Lattice paramter for Mg

	k = 2
	calc = GPAW(mode=PW(200),       # cutoff
		         kpts=(k, k, k),     # k-points
		         txt=name + '.txt',	# output file
			 eigensolver='dav') 

	while (latticeParam <= 5.5):

		# Generate bulk material
		bulk = bulkSC(alloyMix, latticeParam, 2)

		bulk.set_calculator(calc)

		energy = bulk.get_potential_energy()

		energy = energy/nbrPrimCells

		print("%f \t %f" %(energy, latticeParam))

		# New lattice parameter
		latticeParam = latticeParam + 0.1

main()
