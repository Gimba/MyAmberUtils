#! /usr/bin/env python

# Copyright (c) 2017 Martin Rosellen

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

import argparse
import sys

__author__ = 'Martin Rosellen'
__docformat__ = "restructuredtext en"

def main(argv):
    parser = argparse.ArgumentParser(description='Plot residue interactions.')
    parser.add_argument('file_1', help='HBond file 1')
    parser.add_argument('file_2', help='HBond file 2')
    parser.add_argument('outfile', help='outfile')
    args = parser.parse_args()

    labels_1 = []
    values_1 = []
    with open(args.file_1, 'r') as f:
        for line in f:
            temp = str.split(line,',')
            labels_1.append(temp[0]+',' +temp[1])
            values_1.append(temp[2])

    labels_2 = []
    values_2 = []
    with open(args.file_2, 'r') as f:
        for line in f:
            temp = str.split(line,',')
            labels_2.append(temp[0]+','+temp[1])
            values_2.append(temp[2])

    labels = []
    values = []

    for i in range(0,len(labels_1)):
        for j in range(0,len(labels_2)):
            if labels_1[i] == labels_2[j]:
                labels.append(labels_1[i])
                values.append(int(values_1[i]) - int(values_2[j]))

    with open(args.outfile, 'w') as f:
        for i in range(0,len(values)):
            f.write(labels[i] + ',' + str(values[i]) + '\r\n')


if __name__ == "__main__":
    main(sys.argv)