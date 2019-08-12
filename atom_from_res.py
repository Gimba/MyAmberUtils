#! /usr/bin/env python

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
                print(' '.join(line))
                print('Atom number: {}'.format(line[1]))


def main(argv):
    parser = argparse.ArgumentParser(description='Add a chain identifier to specified residue range')
    parser.add_argument('pdb', help='pdb file name')
    parser.add_argument('res', help='residue')
    parser.add_argument('atom_type', help='atom type')

    args = parser.parse_args()

    atom_from_res(args.pdb, args.res, args.atom_type)


if __name__ == '__main__':
    main(sys.argv)
