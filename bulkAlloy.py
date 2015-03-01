from __future__ import print_function
from ase import Atoms

""" Function for generatring a basis for an alloy in SC.

alloyMix : Parameter to determine the mixture between Al and Mg
	   0 = pure Al. 100 = pure Mg [0 25 75 100]
latticeParam : The lattice parameterer in angstrom
latticeConfig : Separates the non-equivalent configurations in 
		the 50/50 case. [1 2]	 

"""
def bulkSC(alloyMix, latticeParam, latticeConfig = 2): 

	# Define alternating atoms 
	def one():
		return(['Mg','Al','Mg','Al'])

	def two():
		return( ['Mg','Al','Al','Mg'])

	atomConfig = {1: one,
 		      2: two,
	} 


	# Define the mixture of the alloy
	def zero():
		return( ['Al','Al','Al','Al'])

	def twentyfive():
		return(['Mg','Al','Al','Al'])

	def fifty():
		return( atomConfig[latticeConfig]())

	def seventyfive():
		return( ['Al','Mg','Mg','Mg'])
		
	def hundred():
		return(['Mg','Mg','Mg','Mg'])

	atomMix = {0: zero,
		   25: twentyfive,
		   50: fifty,
		   75: seventyfive,
		   100: hundred,
		}
		

	# Call alloyMix to get array with atoms
  	atomArray = atomMix[alloyMix]() 

	
	# Create bulk material
	bulk = Atoms(atomArray, 
			positions=[(0,0,0),
				(latticeParam,latticeParam,0),
				(0,0,latticeParam),
				(latticeParam,latticeParam,latticeParam)],
			cell=[2*latticeParam, latticeParam, 2*latticeParam],
			pbc=True) 

	# Return the bulk-material
	return(bulk)

""" Function for generatring a basis for an alloy in BCC.

alloyMix : Parameter to determine the mixture between Al and Mg
	   0 = pure Al. 100 = pure Mg [0 25 75 100]
latticeParam : The lattice parameterer in angstrom
latticeConfig : Seperates the non-equivalent configurations in 
		the 50/50 case. [1 2]	 

"""
def bulkBCC(alloyMix, latticeParam, latticeConfig = 2): 

	# Define alternating atoms 
	def one():
		return (['Mg','Mg','Al','Al'])

	def two():
		return(['Mg','Al','Mg','Al'])

	atomConfig = {1: one,
 		      2: two,
		} # Alternating atoms 



	# Define the mixture of the alloy
	def zero():
		return(['Al','Al','Al','Al'])

	def twentyfive():
		return(['Mg','Al','Al','Al'])

	def fifty():
		return(atomConfig[latticeConfig]())

	def seventyfive():
		return(['Al','Mg','Mg','Mg'])
		

	def hundred():
		return(['Mg','Mg','Mg','Mg'])

	atomMix = {0: zero,
		   25: twentyfive,
		   50: fifty,
		   75: seventyfive,
		   100: hundred,
		}


	# Call alloyMix to get array with atoms
	atomArray = atomMix[alloyMix]()


	# Create bulk material
	bulk = Atoms(atomArray, 
			positions=[(0,0,0),
				(latticeParam,0,0),
				(latticeParam/2,latticeParam/2,latticeParam/2),
				(latticeParam*3/2,latticeParam/2,latticeParam/2)],
			cell=[2*latticeParam, latticeParam, latticeParam],
			pbc=True) 

	# Return the bulk-material
	return(bulk)

""" Function for generatring a basis for an alloy in FCC.

alloyMix : Parameter to determine the muxture between Al and Mg
	   0 = pure Al. 100 = pure Mg [0 25 75 100]
latticeParam : The lattice parameterer in angstrom

"""
def bulkFCC(alloyMix, latticeParam, latticeConfig = 2): 

	def zero():
		return( ['Al','Al','Al','Al'] )

	def twentyfive():
		return( ['Mg','Al','Al','Al'] )

	def fifty():
		return(['Mg','Mg','Al','Al'] )

	def seventyfive():
		return( ['Al','Mg','Mg','Mg'] )

	def hundred():
		return( ['Mg','Mg','Mg','Mg'] )


	# Define the mixture of the alloy
	atomMix = {0: zero,
		   25: twentyfive,
		   50: fifty,
		   75: seventyfive,
		   100: hundred,
		}

	# Call alloyMix to get array with atoms
	atomArray = atomMix[alloyMix]()

	b = latticeParam/2

	# Create bulk material
	bulk = Atoms(atomArray, 
	       	     positions=[(0,0,0),
				(b,b,0),
				(0,b,b),
				(b,0,b)],
            	 	cell=[latticeParam, latticeParam, latticeParam],
               	 	pbc=True) 
	

	# Return the bulk-material
	return(bulk)


def bulkRockSalt(alloyMix, latticeParam):

	def zero():
		return( ['Al','Al','Al','Al','S','S','S','S'] )

	def twentyfive():
		return( ['Mg','Al','Al','Al','S','S','S','S'] )

	def fifty():
		return(['Mg','Mg','Al','Al','S','S','S','S'] )

	def seventyfive():
		return( ['Al','Mg','Mg','Mg','S','S','S','S'] )

	def hundred():
		return( ['Mg','Mg','Mg','Mg','S','S','S','S'] )


	# Define the mixture of the alloy
	atomMix = {0: zero,
		   25: twentyfive,
		   50: fifty,
		   75: seventyfive,
		   100: hundred,
		}

	# Call alloyMix to get array with atoms
	atomArray = atomMix[alloyMix]()
	
	b = latticeParam/2

	# Create bulk material
	bulk = Atoms(atomArray, 
	       	     positions=[(0,0,0),
				(b,b,0),
				(0,b,b),
				(b,0,b),
				(b,b,b),
				(0,b,0),
				(0,0,b),
				(b,0,0)],
            	 	cell=[latticeParam, latticeParam, latticeParam],
               	 	pbc=True) 

	# Return the bulk-material
	return(bulk)
