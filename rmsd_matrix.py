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

__author__ = 'Martin Rosellen'
__docformat__ = "restructuredtext en"

import pytraj as pt
import sys
import matplotlib.pyplot as plt
from pytraj.plot import plot_matrix
import argparse
import re
from multiprocessing import Pool
import csv


def calc_rmsd(trajs):
    return pt.rmsd(trajs[1], "", trajs[0])


def main(argv):
    parser = argparse.ArgumentParser(description='Script to calculate an rmsd matrix for two trajectories')
    parser.add_argument('prmtop_0', help='topology in prmtop format')
    parser.add_argument('traj_0', help='trajectory in format usable with pytraj')
    parser.add_argument('prmtop_1', help='other topology in prmtop format')
    parser.add_argument('traj_1', help='other trajectory in format usable with pytraj')
    parser.add_argument('plot_file', help='file name for matrix plot')
    parser.add_argument('data_file', help='file name for matrix data')
    parser.add_argument('-strip', nargs='*', help='mask to use', default="@CA")
    parser.add_argument('-clim', nargs='*', help='range of values for coloring')
    args = parser.parse_args()

    print("loading trajectory", args.traj_0)
    traj_top_0 = pt.load(args.traj_0, args.prmtop_0)
    # traj_top_0 = pt.strip(traj_top_0, '!@CA')
    # traj_top_0 = pt.strip(traj_top_0, ':142,42,47,77,78,79,80,49,82,143,23,24,25,26,27,50')

    print("loading trajectory", args.traj_1)
    traj_top_1 = pt.load(args.traj_1, args.prmtop_1)
    # traj_top_1 = pt.strip(traj_top_1, '!@CA')
    # traj_top_1 = pt.strip(traj_top_1, ':145,45,50,80,81,82,83,52,85,146,26,27,28,29,30,53')

    print(pt.rmsd(traj_top_0, ":4-159@CA", traj_top_1, ":1-156@CA"))
    exit()

    traj_top_1_list = []
    for j in traj_top_1:
        traj_top_1_list.append(j.copy())

    new_iterable = [[t1, traj_top_0] for t1 in traj_top_1_list]
    rmsds = []
    for i in range(len(new_iterable)):
        rmsds.append(pt.rmsd(new_iterable[i][1],"@CA", new_iterable[i][0]))
    # pool = Pool(1)
    # rmsds = pool.map(calc_rmsd, new_iterable)
    # print(rmsds[0])
    # exit()

    with open(args.data_file, "wb") as f:
        writer = csv.writer(f)
        writer.writerows(rmsds)

    fig, asp, axi, = plot_matrix(list(rmsds))
    cbar = fig.colorbar(axi, ax=asp)
    if args.clim:
        args.clim = list(map(int, re.findall('\d+', args.clim[0])))
        cbar.set_clim(args.clim[0], args.clim[1])
    plt.ylabel(args.prmtop_0.split('.')[0])
    plt.xlabel(args.prmtop_1.split('.')[0])
    plt.savefig(args.plot_file)
    # plt.show()





if __name__ == "__main__":
    main(sys.argv)