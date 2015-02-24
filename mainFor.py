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
	struc = 'SC'

	mix = [50]

	for alloyMix in mix:
		
		
		# CHANGE BEFORE RUNNING THE SCRIPT
		nbrPrimCells = 4

		name = struc+'-'+str(alloyMix)
		latticeParam = 2.0  # Lattice paramter for Mg

		k = 6
		calc = GPAW(mode=PW(300),       	# cutoff
			         kpts=(k, k, k),     	# k-points
			         txt=name + '.txt',	# output file
				 eigensolver='dav') 

		while (latticeParam <= 4.5):

			# CHANGE BEFORE RUNNING THE SCRIPT
			# Generate bulk material			
			bulk = bulkSC(alloyMix, latticeParam, 1)

			bulk.set_calculator(calc)

			energy = bulk.get_potential_energy()

			energy = energy/nbrPrimCells

			print("%f \t %f \t %s \t %d" % (energy, latticeParam,struc, alloyMix))

			# New lattice parameter
			latticeParam = latticeParam + 0.1

main()
