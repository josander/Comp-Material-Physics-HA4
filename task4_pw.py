#!/usr/bin/env python
from ase import *
from ase.io import read,write
import numpy as np
from gpaw import GPAW, restart
from gpaw import PW

mol,calc = restart('out_methane.gpw')

del mol[[1,2,3,4]]
calc=GPAW(mode=PW(200),basis='dzp',spinpol=True,hund=True, h=0.2, xc='PBE', nbands=8, txt='out_taskC_pw.txt')
mol.set_calculator(calc)
mol.get_potential_energy()
calc.write('1C.gpw')

mol,calc = restart('out_methane.gpw')

del mol[[0,2,3,4]]
calc=GPAW(mode=PW(200),basis='dzp',spinpol=True, h=0.2, xc='PBE', nbands=8, txt='out_taskH_pw.txt')
mol.set_calculator(calc)
mol.get_potential_energy()
calc.write('1H.gpw')

mol,calc = restart('out_methane.gpw')

del mol[[0,1,3,4]]
calc=GPAW(mode=PW(200),basis='dzp',spinpol=True,hund=True, h=0.2, xc='PBE', nbands=8, txt='out_task4_pw.txt')
mol.set_calculator(calc)
mol.get_potential_energy()
calc.write('2H.gpw')

mol,calc = restart('out_methane.gpw')

del mol[[0,1,2,4]]
calc=GPAW(mode=PW(200),basis='dzp',spinpol=True,hund=True, h=0.2, xc='PBE', nbands=8, txt='out_task4_pw.txt')
mol.set_calculator(calc)
mol.get_potential_energy()
calc.write('3H.gpw')

mol,calc = restart('out_methane.gpw')

del mol[[0,1,2,3]]
calc=GPAW(mode=PW(200),basis='dzp',spinpol=True,hund=True, h=0.2, xc='PBE', nbands=8, txt='out_task4_pw.txt')
mol.set_calculator(calc)
mol.get_potential_energy()
calc.write('4H.gpw')





