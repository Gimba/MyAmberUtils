#!/usr/bin/env python

# Copyright (c) 2018 Martin Rosellen

# Permission is hereby granted, free of charge, to any person obtaining a
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import numpy as np
import argparse
import sys


def main(args):
    parser = argparse.ArgumentParser(description='prints standard deviation, mean and median to standard out.')
    parser.add_argument('file', help='file containing values in the second column')

    args = parser.parse_args()

    data = []
    with open(args.file, 'r') as f:
        for line in f.readlines():
            line = line.split()
            if len(line) == 2:
                try:
                    data.append(float(line[1]))
                except:
                    pass

        # print("Standard deviation: {:.2f}".format(np.std(data)))
        # print("Mean value: {:.2f}".format(np.mean(data)))
        # print("Median value: {:.2f}".format(np.median(data)))

    print("{:.2f}".format(np.std(data)))
    print("{:.2f}".format(np.mean(data)))
    print("{:.2f}".format(np.median(data)))


if __name__ == '__main__':
    main(sys.argv)
