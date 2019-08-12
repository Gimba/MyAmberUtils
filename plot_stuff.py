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
from matplotlib.cm import get_cmap
import sys
import argparse
import pandas as pd
import numpy as np
import math
plt.rcParams["figure.figsize"] = [16,9]
plt.rcParams["patch.edgecolor"] = 'None'

__author__ = 'Martin Rosellen'
__docformat__ = "restructuredtext en"

def main(argv):
    parser = argparse.ArgumentParser(description='Plot data contained in columns')
    parser.add_argument('infile', help='data')
    parser.add_argument('outfile', nargs='?', help='output file', default="")
    parser.add_argument('-v_lines', nargs='?', help='add v lines to the plots. e.g -11,22,32', default="")
    args = parser.parse_args()


    content = pd.read_csv(args.infile,sep=r'\s* ',header=None, index_col=0, engine='python')
    n_cols = len(content.columns)
    fig, axes = plt.subplots(nrows=n_cols, ncols=2)
    if args.v_lines:
        v_lines = args.v_lines.split(',')

    cmap = get_cmap('Spectral')
    colors = [cmap(1.*i/n_cols) for i in range(n_cols)]
    for i in range(1,n_cols+1):
        col_dat = content.loc[:,i]
        col_dat.plot.hist(bins=180, ax=axes[i-1,0], color=colors[i-1], edgecolor=None)
        col_dat.plot(ax=axes[i-1,1], color=colors[i-1])
        fwhm = 2 * np.sqrt(2 * (math.log(2))) * np.std(col_dat)

        if args.v_lines:
            axes[i-1,0].axvline(v_lines[i-1], color='black')
            axes[i-1,0].text(v_lines[i-1], 0, str(v_lines[i-1]))

        axes[i-1,0].text(0.005, 0.95,'FWHM: ' + str(round(fwhm,2)), horizontalalignment='left',
                         verticalalignment='center',
                         transform = axes[i-1,0].transAxes)
    if args.outfile:
        plt.savefig(args.outfile)
    else:
        f_name = args.infile.split('.')[0] + ".png"
        plt.savefig(f_name)
    # plt.show()

if __name__ == "__main__":
    main(sys.argv)
