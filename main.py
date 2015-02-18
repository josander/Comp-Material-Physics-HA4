from __future__ import print_function
from ase import Atoms
from gpaw import GPAW, PW
from gpaw.eigensolvers import Davidson

""" Function for generatring a basis for an alloy in SC.

alloyMix : Parameter to determine the muxture between Al and Mg
	   0 = pure Al. 100 = pure Mg [0 25 75 100]
latticeParam : The lattice parameterer in Å
latticeConfig : Seperates the non-equivalent configurations in 
		the 50/50 case. [1 2]	 

"""
def bulkSC(alloyMix, latticeParam, latticeConfig): 

	atomConfig = {1: atomArray = ['Mg','Al','Mg','Al'], # Atoms are place along the z-axis
 		      2: atomArray = ['Mg','Al','Al','Mg']} # Alternating atoms 

	atomMix = {0: atomArray = ['Al','Al','Al','Al'],
		   25: atomArray = ['Mg','Al','Al','Al'],
		   50: atomArray = atomConfig[latticeConfig],
		   75: atomArray =['Al','Mg','Mg','Mg'],
		   100: atomArray =['Mg','Mg','Mg','Mg']}

  	atomMix[alloyMix] 


	bulk = Atoms(atomArray, 
			positions=[(0,0,0),
				(latticeParam,latticeParam,0),
				(0,0,latticeParam),
				(latticeParam,latticeParam,latticeParam)],
			cell=[2*latticeParam, latticeParam, 2*latticeParam],
			pbc=True) 
	return(bulk)

""" Function for generatring a basis for an alloy in BCC.

alloyMix : Parameter to determine the muxture between Al and Mg
	   0 = pure Al. 100 = pure Mg [0 25 75 100]
latticeParam : The lattice parameterer in Å
latticeConfig : Seperates the non-equivalent configurations in 
		the 50/50 case. [1 2]	 

"""
def bulkBCC(alloyMix, latticeParam, latticeConfig): 

	atomConfig = {1: atomArray = ['Mg','MG','Al','Al'], # Atoms are place in rows
 		      2: atomArray = ['Mg','Al','Mg','Al']} # Alternating atoms 

	atomMix = {0: atomArray = ['Al','Al','Al','Al'],
		   25: atomArray = ['Mg','Al','Al','Al'],
		   50: atomArray = atomConfig[latticeConfig],
		   75: atomArray =['Al','Mg','Mg','Mg'],
		   100: atomArray =['Mg','Mg','Mg','Mg']}

  	atomMix[alloyMix] 
	

	bulk = Atoms(atomArray, 
			positions=[(0,0,0),
				(latticeParam,0,0),
				(latticeParam/2,latticeParam/2,latticeParam/2),
				(latticeParam*3/2,latticeParam/2,latticeParam/2)],
			cell=[2*latticeParam, latticeParam, latticeParam],
			pbc=True) 

	return(bulk)

""" Function for generatring a basis for an alloy in FCC.

alloyMix : Parameter to determine the muxture between Al and Mg
	   0 = pure Al. 100 = pure Mg [0 25 75 100]
latticeParam : The lattice parameterer in Å 

"""
def bulkFCC(alloyMix, latticeParam): 

	atomMix = {0: atomArray = ['Al','Al','Al','Al'],
		   25: atomArray = ['Mg','Al','Al','Al'],
		   50: atomArray = ['Mg','Mg','Al','Al'],
		   75: atomArray =['Al','Mg','Mg','Mg'],
		   100: atomArray =['Mg','Mg','Mg','Mg']}

  	atomMix[alloyMix] 
	bulk = Atoms(atomArray, 
	       	     positions=[(0,0,0),
				(latticeParam/2,latticeParam/2,0),
				(0,latticeParam/2,latticeParam/2),
				(latticeParam/2,0,latticeParam/2)],
            	 cell=[latticeParam, latticeParam, latticeParam],
               	 pbc=True) 
	
	return(bulk)

def main():
	print('hej')

main()
