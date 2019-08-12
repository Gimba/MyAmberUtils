#! /usr/bin/env python

import sys
import argparse
from os import remove


def main(argv):
    parser = argparse.ArgumentParser(description='Add a chain identifier to specified residue range')
    parser.add_argument('file', help='pdb file name')
    parser.add_argument('res1', help='first residue')
    parser.add_argument('res2', help='last residue')
    parser.add_argument('chain_id', help='chain id')

    args = parser.parse_args()

    res1 = int(args.res1) - 1
    res2 = int(args.res2) + 1
    chain_id = args.chain_id
    pdb = args.file

    out = ""

    with open(pdb, 'r') as f:

        for line in f.readlines():
            if line[:4] == 'ATOM':
                line_split = line.split()
                line_res = int(line_split[4])
                if line_res > res1 and line_res < res2:
                    out += line[:21] + chain_id + line[22:]
                    print(out)
            elif line[:3] == 'TER':
                line_split = line.split()
                line_res = int(line_split[3])
                if line_res > res1 and line_res < res2:
                    out += line[:21] + chain_id + line[22:]
                    print(out)
            else:
                out += line
    remove(pdb)

    with open(pdb, 'w') as o:
        o.write(out)


if __name__ == '__main__':
    main(sys.argv)
