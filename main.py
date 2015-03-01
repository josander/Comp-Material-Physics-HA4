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
	# Percentage of magnesium in the substrate X, such that the compound is X and S
	alloyMix = 100 
	struc = 'Rock'

	name = struc+'-'+str(alloyMix)
	latticeParam = 4.3  # Best lattice parameter

	# Generate bulk material
	bulk = bulkRockSalt(latticeParam)

	# Define the calculator-object
	k = 8
	calc = GPAW(mode=PW(400),       	# cutoff
		         kpts=(k, k, k),     	# k-points
			 nbands = 64,		# number of bands
		         txt=name + '.txt',	# output file
			 eigensolver='dav') 

	# Create calc-object
	bulk.set_calculator(calc)

	# Get potential energy
	energy = bulk.get_potential_energy()

	# Get energy per primitive cell
	energy = energy

	# Define calc-file
	fileName = name+'.gpw'

	# Save calculator to be able to plot the bandgap
	calc.write(fileName, mode='all')

main()
