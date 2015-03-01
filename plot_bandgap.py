#!/usr/bin/env python
from ase import * 
from ase.dft.dos import DOS
from gpaw import GPAW, restart 
import pylab as p

slab, calc = restart('Rock-75.gpw')
e, dos = calc.get_dos(spin=0, npts=2001, width=0.1)
e_f = calc.get_fermi_level()

p.subplot(211)
p.plot(e-e_f, dos)
p.grid(True)
p.axis([-15, 10, None, None])
p.ylabel('DOS')

p.subplot(212)
p.plot(e-e_f, dos)
p.grid(True)
p.axis([-1, 1, None, None])
p.ylabel('DOS')
p.show()


