#! /usr/bin/env python

# Copyright (c) 2017 Martin Rosellen

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys
import argparse
import os
from collections import defaultdict
from collections import OrderedDict
import re
from scipy.stats.stats import pearsonr

__author__ = 'Martin Rosellen'
__docformat__ = "restructuredtext en"

def main(argv):
    parser = argparse.ArgumentParser(description='Calculate AMD parameters from .out file.')
    parser.add_argument('out_file', help='')

    args = parser.parse_args()

    file = args.out_file

    n_atoms = 0
    n_res = 156
    ethreshp = 0
    ethreshd = 0
    alphad = 0
    alphap = 0

    with open(file, 'r') as f:
        content = f.readlines()
        line_counter = 0
        for line in content:
            line_counter += 1
            if "NATOM" in line:
                n_atoms = line.split()[2]
            if "      A V E R A G E S   O V E R     " in line:
                avg_line = content[line_counter+3].split()
                eptot = avg_line[-1]
                dihed = avg_line = content[line_counter+4].split()[-1]

    res_cal = 3.5 * n_res

    alphad = int(0.2 * res_cal)
    ethreshd = int(res_cal + float(dihed))

    alphap = int(0.2 * int(n_atoms))
    ethreshp = int(float(eptot) + alphap)

    print alphad
    print ethreshd
    print alphap
    print ethreshp
if __name__ == "__main__":
    main(sys.argv)