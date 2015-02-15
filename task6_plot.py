from ase.io import read 
from ase.units import kJ
from ase.utils.eos import EquationOfState

configs = read('Silicon.traj@0:7')  # read 7 configurations

# Extract volumes and energies:
volumes = [atoms.get_volume() for atoms in configs]
energies = [atoms.get_potential_energy() for atoms in configs]

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
print v0, 'AA', B / kJ * 1.0e24, 'GPa'
eos.plot('Silicon-eos.png')

