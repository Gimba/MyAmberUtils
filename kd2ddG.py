#! /usr/bin/env python

import sys
import math

def kd2ddg(kd, temp=300.0):
    gas_const = 8.3144621

    to_kcal = 0.23900574 / 1000

    dd_G = gas_const * temp * math.log(kd) * to_kcal

    return dd_G

def main(argv):
    kd = float(sys.argv[1])
    if len(sys.argv) > 2:
        temp = float(sys.argv[2])
    else:
        temp = 300

    dd_G = kd2ddg(kd, temp)

    print str(dd_G) + " kcal/mol"

if __name__ == '__main__':
    main(sys.argv)