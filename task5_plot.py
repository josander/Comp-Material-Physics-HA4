from ase.io import read,write
from ase.optimize import BFGS
from ase.data.molecules import molecule
from enthought.mayavi.mlab import *
import numpy as np
from gpaw import GPAW, restart
from gpaw import PW

mol,calc = restart('CH4_SCF.008.gpw')
cell=mol.get_cell()
n = calc.get_pseudo_density()

N = len(n[0,:,:])
X, Y, Z = np.mgrid[0:(cell[0,0]-cell[0,0]/N):N*1j,\
                   0:(cell[1,1]-cell[1,1]/N):N*1j,\
                   0:(cell[2,2]-cell[2,2]/N):N*1j]

figure('Pseudo charge density for CH4')
contour3d(X, Y, Z, n, contours =24, transparent=True , opacity=0.3)

for atom in mol:
  symbol , pos = atom.get_symbol(), atom.get_position()
  if symbol == 'C':
    color = (0,0,0)
  points3d (pos[0], pos[1], pos[2], color=color, resolution=64, scale_factor=0.3 )
  if symbol == 'H':
    color = (0,0,1)
  points3d (pos[0], pos[1], pos[2], color=color, resolution=64, scale_factor=0.3 )



colorbar()
show()






