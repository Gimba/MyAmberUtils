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

# import argparse
# import os
# import re
import sys
# from collections import Counter


__author__ = 'Martin Rosellen'
__docformat__ = "restructuredtext en"


def main(argv):
    out = ""
    with open("./productions/mmpbsa_all_frames/frame_energies.csv", 'r') as f:
        with open("./productions/binding_site_distances.dat", 'r') as g:

            # skip lines until delta energies begin
            line = ""
            while 'DELTA' not in line:
                line = f.readline()
            print(line)
            header_f = f.readline()
            header_g = g.readline()
            header_f = header_f.split(',')
            header_g = header_g.split()
            header = header_f[0] + ',' + ','.join(header_g[1:]) + ',' + header_f[-1]
            out += header
            for energy, distances in zip(f.readlines(),g.readlines()):
                energy = energy.split(',')

                distances = distances.split()
                out += energy[0]+ ',' + ','.join(distances[1:]) + ',' + energy[-1]
            print(out)
            with open("./training_data_dist_energy.csv", "w") as o:
                o.write(out)


if __name__ == "__main__":
    main(sys.argv)
