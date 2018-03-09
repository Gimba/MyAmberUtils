#! /usr/bin/env python

from scipy import stats
import sys
import numpy as np

cryst = [-95.43, -88.79, -96.35, -97.23, -96.01, -96.23, -84.05, -86.76, -93.28, -98.51, -92.14, -94.49]
cryst = [item + 94.49 for item in cryst]

back_muta = [-91.40, -93.22, -98.73, -104.4, -94.88, -92.40, -73.53, -88.90, -92.20, -97.66, -104.0, -102.26]
back_muta = [item + 102.26 for item in back_muta]

experiment = [1.3012, 2.9955, 1.3637, 2.3839, 3.2458, 2.9674, 0.9532, 1.0611, 1.8306, 1.3637, 0.4105, 0.9532]



print("crystal structure")
print(stats.spearmanr(experiment, cryst))
print("back_muta")
print(stats.spearmanr(experiment, back_muta))

# print(stats.wilcoxon(experiment, cryst, zero_method="wilcox"))
