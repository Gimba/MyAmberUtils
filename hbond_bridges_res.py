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

# This program is intended to replace specified residues with those generated from a modeller run.
# imported atom numbers are set to zero, to avoid conflicts with CONECT records in the original file.

__author__ = 'Martin Rosellen'
__docformat__ = "restructuredtext en"

import argparse
import os
import sys

def main(argv):
    parser = argparse.ArgumentParser(description='Extract hbond bridges of specified residue from given '
                                                 'bridgeout-file from cpptraj. Result gets written to bridge_file + '
                                                 'res_num')
    parser.add_argument('bridgeout_file', help='name of cpptraj bridgeout file')
    parser.add_argument('res_num', help='number of residue')

    args = parser.parse_args()

    bridges = []
    total = 0

    file_out = args.bridgeout_file.split('.')[0] + "_" + args.res_num + "." + args.bridgeout_file.split('.')[1]
    with open(args.bridgeout_file, 'r') as f:
        for line in f.readlines():
            l = line.split()
            if args.res_num + ':' in l[2]:
                bridges.append(l[2] + " " + l[3] + " " + l[-2])
                total += int(l[-2])

    with open(file_out, 'w') as o:
        o.write('\n'.join(bridges))
        o.write('\ntotal:' + str(total) + '\npercentage: '+ str(total*100/150) + '%')
        print(str(total*100/150))

if __name__ == '__main__':
    main(sys.argv)