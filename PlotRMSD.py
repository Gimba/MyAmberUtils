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

import matplotlib.pyplot as plt
import os
import sys
import argparse
import numpy as np

__author__ = 'Martin Rosellen'
__docformat__ = "restructuredtext en"

def main(argv):
    parser = argparse.ArgumentParser(description='Plot RMSDs of hairpin region with title extracted '
                                                 'from the working directory.')
    parser.add_argument('infile', help='RMSD values from hairpin_rmsd.cpptraj')
    parser.add_argument('outfile', help='File the plot gets saved to')
    parser.add_argument('num', help='Number of productions used for the calculation')
    args = parser.parse_args()


    cwd = os.getcwd()
    mutation = cwd.split("/")[-1]
    super = cwd.split("/")[-2]
    title = (super + " " + mutation + ": Production 1-" + args.num + "\n RMSD values of hairpin region (2186-2210)")

    values = []

    with open(args.infile,'r') as f:
        f.readline()
        for line in f:
            values.append(float(line.split("    ")[2][3:-1]))

    mean = np.mean(values)
    variance = np.var(values)
    caption = "variance: " + str(variance)

    plt.axhline(mean, color='g')
    plt.ylabel("rmsd value")
    plt.xlabel("frame")
    plt.plot(values)

    pos = plt.xlim()[1]
    plt.text(pos/2,0.62,str(caption),ha='center')
    plt.text(pos,mean," " + str(round(mean,2)),va='center')

    plt.ylim([0.6,1.6])
    plt.title(title)
    plt.savefig(args.outfile)

    
if __name__ == "__main__":
    main(sys.argv)
