#!/usr/bin/env python
from ase import Atom, Atoms
from ase.optimize.fire import FIRE
from ase.constraints import StrainFilter
from gpaw import GPAW
from gpaw import PW
from gpaw import FermiDirac
from gpaw import Mixer
from gpaw.eigensolvers import CG

element1=['Mo']
element2=['Mo', 'Ti', 'Cu', 'C']
a = 3.16  # approximate lattice constant
mixer=Mixer(beta=0.05, nmaxold=10, weight=100.0)

for e1 in element1:
  for e2 in element2:
    bulk = Atoms([Atom(e1,(0,0,0)),
                  Atom(e2, (a/2,a/2,a/2))],
                  cell=(a,a,a), pbc=1)
    calc=GPAW(mode=PW(400),                # Energycutoff for planewaves [eV] 
              basis='dzp',
              h=0.2,                       # The distance between gridpoints AA^-1
              xc='PBE',                    # xc-functional
              mixer=mixer,
              eigensolver=CG,
              nbands=40,                   # number of bands
              kpts=(12,12,12),             # number of k-points
              occupations=FermiDirac(0.2), # Fermi temperature [eV]
              txt='out_task7_'+str(e1)+'.'+str(e2)+'.txt')

    bulk.set_calculator(calc)

    sf = StrainFilter(bulk)
    qn = FIRE(sf)
    qn.run(fmax=0.05)  #force is really a stress here

    print bulk.get_cell()
    print bulk.get_stress()
