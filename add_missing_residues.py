#! /usr/bin/env python

# Copyright (c) 2020 Martin Rosellen

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

__author__ = 'Martin Rosellen'
__docformat__ = "restructuredtext en"

import sys
import argparse
import pytraj as pt


def missing_elements(L):
    start, end = L[0], L[-1]
    return sorted(set(range(start, end + 1)).difference(L))


def main(args):
    parser = argparse.ArgumentParser(description='Insert missing residue coordinates using Modeller')
    parser.add_argument('pdb_file', help='pdb_file with missing residues')
    args = parser.parse_args()

    file = args.pdb_file

    residues = {}
    with open(file, 'r') as f:
        for line in f.readlines():
            if line[:4] == 'ATOM':
                residues[line[21] + str(int(line[22:27]))] = line[17:20]
    chains = list(set([r[0] for r in residues.keys()]))

    for c in chains:
        resids = [int(ri[1:]) for ri in residues.keys() if c == ri[0]]
        print(c, missing_elements(resids))


if __name__ == '__main__':
    main(sys.argv)
