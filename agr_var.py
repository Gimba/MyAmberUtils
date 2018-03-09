#! /usr/bin/env python

import numpy
import sys
import argparse

def main(argv):
    parser = argparse.ArgumentParser(description='Calculate the variance in values from a .agr file')
    parser.add_argument('file', help='file name')

    args = parser.parse_args()

    f = open(args.file, "r")
    content = f.readlines()

    content = [item for item in content if '@' not in item]

    content = [item.split()[1] for item in content]

    content = [float(item) for item in content]

    content.pop(0)

    print numpy.var(content)

    out_file = args.file.replace(".agr", "_var.dat")

    o = open(out_file, "w")

    o.write(str(numpy.var(content)))


if __name__ == "__main__":
    main(sys.argv)
