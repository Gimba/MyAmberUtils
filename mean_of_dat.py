#!/usr/bin/env python

import sys, argparse
import numpy as np


def main(args):
    parser = argparse.ArgumentParser(description='Calculate mean of .dat file produced by cpptraj')
    parser.add_argument('file', help='the .dat filename')

    args = parser.parse_args()

    with open(args.file, 'r') as f:
        all_values = []

        for line in f.readlines():
            if line[0] == '#':
                continue
            else:
                line = line.split()
                frame = line[0]
                values = float(line[1])
                all_values.append(values)
    print(np.mean(all_values))

if __name__ == '__main__':
    main(sys.argv)