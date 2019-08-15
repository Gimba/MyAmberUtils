#! /usr/bin/env python

import numpy as np
import argparse

data = []
with open('dihedral_26,27,34,50.dat', 'r') as f:
	for line in f.readlines():
		line = line.split()
		if len(line) == 2:
			try:
				data.append(float(line[1]))
			except:
				pass
print(np.std(data))
print(np.mean(data))
