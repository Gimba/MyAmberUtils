#! /usr/bin/env python

import sys
import argparse
import glob


def main(argv):
    parser = argparse.ArgumentParser(description='Calculate the variance in values from a .agr file')
    parser.add_argument('file', help='file name')

    args = parser.parse_args()
    fls = glob.glob(args.file)
    for f in fls:
        f = open(args.file, "r")
        last = f.readlines()[-1].decode()
        print("mean: " + last.split()[2])
        err = (float(last.split()[3]) + float(last.split()[4].strip('-'))) / 2
        print("var: " + str(err))

if __name__ == "__main__":
    main(sys.argv)

