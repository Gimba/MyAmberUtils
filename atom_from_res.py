#! /usr/bin/env python

import sys
import argparse
from os import remove


def main(argv):
    parser = argparse.ArgumentParser(description='Add a chain identifier to specified residue range')
    parser.add_argument('pdb', help='pdb file name')
    parser.add_argument('res', help='residue')
    parser.add_argument('atom_type', help='atom type')

    args = parser.parse_args()

    with open(args.pdb, 'r') as f:
        for line in f.readlines():
            line = line.split()

            # handle different indices for residue ids if there is no chain id
            if len(line) == 11:
                res_column = 4
            else:
                res_column = 5

            if len(line) > 5 and line[res_column] == args.res and line[2] == args.atom_type:
                print(' '.join(line))
                print('Atom number: {}'.format(line[1]))

if __name__ == '__main__':
    main(sys.argv)

