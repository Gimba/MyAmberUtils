#! /usr/bin/env python

import sys
import argparse
import glob
from numpy import arange, array, ones, linalg, mean, var
# from matplotlib.pyplot import plot, show

def main(argv):
    parser = argparse.ArgumentParser(description='Calculate the variance and mean of values from a .agr file')
    parser.add_argument('file', help='file name')
    args = parser.parse_args()
    fls = glob.glob(args.file)
    for f in fls:
        f = open(args.file, "r")
        content = f.readlines()

        temp_values = []

        for line in content:
            if "legend" in line and "[" in line:
                name = line.split()[3].replace("\"", "")
                if temp_values:
                    print("mean: " + str(mean(temp_values)))
                    print("variance: " + str(var(temp_values)))
                    xi = arange(0, len(temp_values))
                    A = array([xi, ones(len(temp_values))])
                    # linearly generated sequence
                    w = linalg.lstsq(A.T, temp_values)[0]  # obtaining the parameters

                    print('a: {0:02f}'.format(w[0]))
                    print('b: {0:02f}'.format(w[1]))

                    temp_values = []
                print(name)

            if '@' not in line and '#' not in line:
                temp_values.append(float(line.split()[1]))

        if temp_values:
            print("mean: " + str(mean(temp_values)))
            print("variance: " + str(var(temp_values)))
            xi = arange(0, len(temp_values))
            A = array([xi, ones(len(temp_values))])
            # linearly generated sequence
            w = linalg.lstsq(A.T, temp_values)[0]  # obtaining the parameters

            print('a: {0:02f}'.format(w[0]))
            print('b: {0:02f}'.format(w[1]))

            # plotting the line
            # line = w[0] * xi + w[1]  # regression line
            # plot(xi, line, 'r-', xi, temp_values, ' ')
            # show()

        print("\n")

if __name__ == "__main__":
    main(sys.argv)

