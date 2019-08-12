#! /usr/bin/env python

# Copyright (c) 2018 Martin Rosellen

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
from os import remove


def atom_from_res(pdb, res, atom_type):
    """
    Returns the atom number in the pdb file of a given residue with number 'res' and type 'atom_type'

    e.g. atom_from_res('WT.pdb', '29', 'CA')

    :param pdb: file in pdb format
    :param res: residue number
    :param atom_type: atom type
    :return: atom numer
    """
    with open(pdb, 'r') as f:
        for line in f.readlines():
            line = line.split()

            # handle different indices for residue ids if there is no chain id
            if len(line) == 11:
                res_column = 4
            else:
                res_column = 5

            if len(line) > 5 and line[res_column] == res and line[2] == atom_type:
                return line[1]


def main(argv):
    parser = argparse.ArgumentParser(description='Add a chain identifier to specified residue range')
    parser.add_argument('pdb', help='pdb file name')
    parser.add_argument('res', help='residue')
    parser.add_argument('atom_type', help='atom type')

    args = parser.parse_args()

    atom_number = atom_from_res(args.pdb, args.res, args.atom_type)

    print('Atom number: {}'.format(atom_number))


if __name__ == '__main__':
    main(sys.argv)
