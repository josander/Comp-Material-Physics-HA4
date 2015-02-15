#!/usr/bin/env python
import numpy as np
import pylab as p

data = np.genfromtxt('elementoutput.txt', dtype=np.str)

bulkmodulus = np.double(data[:,2])
density = np.double(data[:,1])
labels = data[:,0]

p.figure(1)
for i in range(len(bulkmodulus)):
  p.plot(density[i],bulkmodulus[i],'ok')
  p.text(density[i],bulkmodulus[i],labels[i])

p.plot([min(density)*0.9,max(density)*1.1],[bulkmodulus[0], bulkmodulus[0]])
p.xlim([min(density)*0.9,max(density)*1.1])
p.ylim([min(bulkmodulus)*0.9,max(bulkmodulus)*1.1])
p.title('Material design of alloys')
p.ylabel('Bulk modulus [GPa]'); p.xlabel('Density [kg/m^3]')
p.show()
