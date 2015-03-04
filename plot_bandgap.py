#!/usr/bin/env python
from ase import * 
from ase.dft.dos import DOS
from gpaw import GPAW, restart 
import pylab as p

slab, calc = restart('Rock-75.gpw')
e, dos = calc.get_dos(spin=0, npts=1001, width=0.1)
e_f = calc.get_fermi_level()

slab100, calc100 = restart('Rock-100.gpw')
e100, dos100 = calc100.get_dos(spin=0, npts=2001, width=0.1)
e_f100 = calc100.get_fermi_level()

bulk75 = p.plot(e-e_f, dos, label='AlMgS, E_f = %.1f eV' %(e_f))
bulk100 = p.plot(e100-e_f100, dos100, label='MgS, E_f = %.1f eV' %(e_f100))
p.grid(True)
p.axis([-15, 15, -1, 8])
p.ylabel('DOS')
p.xlabel('Energy difference relative the Fermi energy [eV]')
p.title('Density of states')
p.savefig('DOS.eps')

p.legend()

p.show()


