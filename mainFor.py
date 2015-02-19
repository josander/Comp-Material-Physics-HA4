from __future__ import print_function
from ase import Atoms
from gpaw import GPAW, PW
from gpaw.eigensolvers import Davidson
from bulkAlloy import *


"""
Main-function
"""
def main():
	
	mix = [0, 25, 50, 75, 100]
	# Change these before running the script !!!	
	struc = 'FCC'

	for alloyMix in mix:
		
		
		# Change these before running the script !!!
		nbrPrimCells = 1

		name = struc+'-'+str(alloyMix)
		latticeParam = 3.0  # Lattice paramter for Mg

		k = 10
		calc = GPAW(mode=PW(300),       # cutoff
			         kpts=(k, k, k),     # k-points
			         txt=name + '.txt',	# output file
				 eigensolver='dav') 

		while (latticeParam <= 5.5):

			# Generate bulk material
			# Change these before running the script !!!			
			bulk = bulkFCC(alloyMix, latticeParam, 2)

			bulk.set_calculator(calc)

			energy = bulk.get_potential_energy()

			energy = energy/nbrPrimCells

			print("%f \t %f \t %d" % (energy, latticeParam, alloyMix))

			# New lattice parameter
			latticeParam = latticeParam + 0.1

main()
