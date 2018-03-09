#! /usr/bin/env python

import sys
import math

kd = float(sys.argv[1])
if len(sys.argv) > 2:
    temp = float(sys.argv[2])
else:
    temp = 300

gas_const = 8.3144621

to_kcal = 1000 * 4.1858

dd_G = gas_const * temp * math.log(kd) / to_kcal

print str(dd_G) + " kcal/mol"
