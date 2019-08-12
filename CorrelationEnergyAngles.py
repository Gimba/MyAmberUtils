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
    parser = argparse.ArgumentParser(description='Calculate correlation between given energies and the angle '
                                                 'values in the files specified by the "file_ending" argument. The '
                                                 'number of energy values must be the same as the number of files '
                                                 'that are in the folder and/or subfolder of the working directory of '
                                                 'the script (e.g. CorrelationEnergyAngles.py is started from a '
                                                 'folder that contains 6 subfolders, each subfolder contains one file '
                                                 'with the given ending. As a consequence there have to be 6 energy '
                                                 'values that belong to the files.')
    parser.add_argument('energy_file', help='energy values (line example: F2196A -96.03 0.94 0.92)')
    parser.add_argument('file_ending', help='name endings of files containing angle values, e.g. standard deviation ('
                                            'example: '
                                            '"_angle_stdev.dat"')
    parser.add_argument('outfile', help='output file')

    args = parser.parse_args()
    angle_files = []

    order = []
    file_ends = args.file_ending
    energy_file = args.energy_file

    for root, dirs, files in os.walk("."):
        for name in files:
            if name.endswith(file_ends):
                angle_files.append(str(os.path.join(root, name)))
                order.append(root[2:])
    angles = defaultdict(list)
    order.sort()
    angle_files.sort()

    for file in angle_files:
        with open (file, 'r') as f:
            content = f.readlines()
            for a_line in content:
                temp = a_line.split()
                angles[temp[0]].append(temp[1])

    energies = {}

    with open(energy_file, "r") as g:
        content = g.readlines()
        # get rid of empty lines
        content = filter(None, (line.rstrip() for line in content))
        for e_line in content:
            temp = e_line.split()
            energies[temp[0]] = temp[1]

    energies = OrderedDict(sorted(energies.items()))

    if len(energies.items()) != len(angle_files):
        print "Number of energies not equals number of found files!"
        print "energies " + str(len(energies.items()))
        print "angles " + str(len(angle_files))
        return

    energies = [float(i[1].replace(',','.')) for i in energies.items()]

    bad_chars = '(),'
    out = ""
    for item in angles:
        name = item
        values = [float(j) for j in angles[item]]
        corr = pearsonr(energies, values)
        out += name + " " + str(corr) + "\n"
        # output += name +

    out = out.translate(None, "(),")
    out = out.replace(".", ",")
    with open(args.outfile, 'w') as o:
        o.write(out)

if __name__ == "__main__":
    main(sys.argv)