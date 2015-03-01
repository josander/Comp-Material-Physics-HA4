#!/usr/bin/env python
import pickle
import numpy as np
from ase.dft.kpoints import ibz_points, get_bandpath
from gpaw import GPAW
from gpaw.eigensolvers import CG

alloyMix = 100 
struc = 'Rock'

name = struc+'-'+str(alloyMix)

points = ibz_points['fcc']
G = points['Gamma']
X = points['X']
W = points['W']
K = points['K']
L = points['L']

calc = GPAW(name+'.gpw',
            txt=name+'BS.txt',
            parallel={'domain': 1},
            fixdensity=True,
            usesymm=None,
	    eigensolver= 'cg',
            maxiter=250,
            convergence={'bands': 8})

kpts, x, X = get_bandpath([W, L, G, X, W, K], calc.atoms.cell)
calc.set(kpts=kpts)
calc.get_potential_energy()
e_kn = np.array([calc.get_eigenvalues(k) for k in range(len(kpts))])
pickle.dump((x, X, e_kn), open('eigenvalues100.pckl', 'w'))
