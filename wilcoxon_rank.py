#! /usr/bin/env python

# Copyright (c) 2019 Martin Rosellen

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
import scipy.stats as s
import numpy as np
import random
import matplotlib.pyplot as plt

def main(argv):
    # parser = argparse.ArgumentParser(description='Script to check for hydrogen binding between watermolecules between 2 given residue masks.')
    # parser.add_argument('list1', help='parm file')
    # parser.add_argument('list2', help='trajectory')
    # args = parser.parse_args()


    # cs25, cs37, csWT2025, bm25, bm37
    # F2196A, F2200A, M2199A, N2198A, R2215A, R2220A, R2220Q
    pred = [-91.89, -91.75, -93.66, -101.03, -77.20, -87.68, -84.73, -95.43, -88.79, -88.61, -96.01, -84.05, -86.76,
            -84.74, -91.89, -91.75, -93.66, -101.03, -77.20, -87.68, -84.73, -95.43, -88.79, -88.61, -96.01, -84.05,
            -86.76, -84.74, -93.51, -93.15, -92.58, -99.62, -83.30, -79.58, -93.05, -96.03, -90.28, -94.27, -98.19,
            -74.10, -74.79, -87.76, -91.40, -93.22, -96.19, -94.88, -73.53, -75.90, -87.90]
    exp = [154, 230, 30, 68, 100, 999, 999, 154, 230, 30, 68, 100, 999, 999,154, 230, 30, 68, 100, 999, 999, 154,
           230, 30, 68, 100, 999, 999, 154, 230, 30, 68, 100, 999, 999, 154, 230, 30, 68, 100, 999, 999, 154, 230, 30, 68, 100, 999, 999]
    diff  = np.asarray(pred) - np.asarray(exp)
    plt.hist(diff)
    # plt.plot(exp)
    plt.show()
    print(len(exp),len(pred))
    print(s.wilcoxon(pred, exp))

if __name__ == '__main__':
    main(sys.argv)