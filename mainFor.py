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
	struc = 'Rock'
	mix = [75, 100]

	for alloyMix in mix:

		name = struc+'-'+str(alloyMix)
		latticeParam = 4.5  # Lattice paramter for Mg

		k = 10
		calc = GPAW(mode=PW(500),       	# cutoff
			         kpts=(k, k, k),     	# k-points
			         txt=name + '.txt',	# output file
				 eigensolver='dav') 

		while (latticeParam <= 5.5):

			# CHANGE BEFORE RUNNING THE SCRIPT
			# Generate bulk material			
			bulk = bulkRockSalt(alloyMix, latticeParam)

			bulk.set_calculator(calc)

			energy = bulk.get_potential_energy()

			print("%f \t %f \t %d" %(energy, latticeParam, alloyMix))

			# New lattice parameter
			latticeParam = latticeParam + 0.1

main()
