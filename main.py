from __future__ import print_function
from ase import Atoms
from gpaw import GPAW, PW
from gpaw.eigensolvers import Davidson
from bulkAlloy import *
from ase.io.trajectory import PickleTrajectory
import numpy as np


"""
Main-function
"""
def main():

	# CHANGE BEFORE RUNNING THE SCRIPT
	# Percentage of magnesium in the substrate X, such that the compound is X and S
	alloyMix = 75 
	struc = 'Rock'

	name = struc+'-'+str(alloyMix)
	latticeParam = 4.3  # Best lattice parameter

	# Generate bulk material
	bulk = bulkRockSalt(alloyMix,latticeParam)

	#
	cell = bulk.get_cell()
	traj = PickleTrajectory(name + '.traj', 'w')

	# Define the calculator-object
	k = 10
	calc = GPAW(mode=PW(500),       	# cutoff
		         kpts=(k, k, k),     	# k-points
			 nbands = 64,		# number of bands, rock should be 64
		         txt=name + '.txt',	# output file
			 eigensolver='dav') 

	# Create calc-object
	bulk.set_calculator(calc)

	# Get potential energy
	energy = bulk.get_potential_energy()

	# Define calc-file
	fileName = name+'.gpw'

	# Save calculator to be able to plot the bandgap
	calc.write(fileName, mode='all')

	# Save the traj-file
	for x in np.linspace(0.95, 1.05, 7):
	  bulk.set_cell(cell * x, scale_atoms=True)
	  traj.write(bulk)

main()
