import pickle
import matplotlib.pyplot as plt
from ase import * 
from ase.dft.dos import DOS
from gpaw import GPAW, restart 
import pylab as p

# CHANGE THIS
mix = 75

slab, calc = restart('Rock-75.gpw')
e, dos = calc.get_dos(spin=0, npts=2001, width=0.1)
e_f = calc.get_fermi_level()

point_names = ['W','L','\Gamma','X','W','K']
x, X, e_kn = pickle.load(open('eigenvaluesMany75.pckl'))
e_kn -= e_f
emin = e_kn.min() - 1
emax = e_kn.max() + 1 
plt.figure(figsize=(6, 4))

for n in range(40):
  plt.plot(x, e_kn[:, n], )
for p in X:
  plt.plot([p, p], [emin, emax],'k-')

#100
#plt.plot([0, X[-1]], [-1.441, -1.441],'g--')
#plt.plot([0, X[-1]], [1.240, 1.240],'g--')

plt.xticks(X, ['$%s$'% n for n in point_names])
plt.axis(xmin=0, xmax=X[-1], ymin=-20, ymax=10)
plt.xlabel('k-vector')
plt.ylabel('Energy difference relative the Fermi energy [eV]')
plt.title('PBE bandstructure of AlMgS')
# CHANGE THIS
plt.savefig('AlMg3S4.png')

plt.show()
