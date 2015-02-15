#!/usr/bin/env python
from ase import *
from ase.calculators.jacapo import *
from ase.utils.eos import *
from ase.io import PickleTrajectory

element1 = ['Mo']
element2 = ['Mo', 'Ti', 'Cu', 'C']
output = open('elementoutput.txt', 'w')

for e1 in element1:
  for e2 in element2:
    calc=Jacapo('out.'+str(e1)+'.'+str(e2)+'.nc')
    atoms=calc.get_atoms()
    cell = atoms.get_cell()

    vols = []
    energies = []

    traj = PickleTrajectory(str(e1)+'.'+str(e2)+'.traj', 'w')
    for x in np.linspace(0.95, 1.05, 5):
      atoms.set_cell(cell * x, scale_atoms=True)
      traj.write(atoms)
      
      vols.append(atoms.get_volume())
      energies.append(atoms.get_potential_energy())

    eos = EquationOfState(vols, energies)
    v0, e0, B = eos.fit()
    mass=atoms.get_masses()[0]+atoms.get_masses()[1]
    # Print the combination, density, and bulk modulus
    print  >>output, str(e1)+str(e2), mass/v0*1.66e-27/1e-30, B/ kJ * 1.0e24