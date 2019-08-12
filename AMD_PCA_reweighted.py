#! /usr/bin/env python

# Copyright (c) 2018 Martin Rosellen

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

import sys, argparse, os

def main(args):
    parser = argparse.ArgumentParser(description='Create that fancy heatmaps from the Amber tutorial')
    parser.add_argument('amd_log', help='the amd.log file')
    parser.add_argument('pca_data', help='pca plot from cpptraj')
    parser.add_argument('pca_out', help='pca data outfile')

    args = parser.parse_args()

    # transform amd_log (AMBER14)
    # For AMBER14:
    # awk 'NR%1==0' amd.log | awk '{print ($8+$7)/(0.001987*300)" " $2 " " ($8+$7)}' > weights.dat

    os.system('awk \'NR%1==0\' ' + args.amd_log + ' | awk \'{print ($8+$7)/(0.001987*300)\" \" $2 \" \" ($8+$7)}\' > ' \
                                                  'weights.dat')


    with open('weights.dat', 'r') as wi:
        w = wi.readlines()[3:]

    with open('weights.dat', 'w') as wo:
        wo.writelines(w)

    out_string = ""
    with open(args.pca_data, 'r') as f:
        for line in f:
            line = line.split()
            if len(line) > 2:
                try:
                    pca_1 = float(line[1])
                    pca_2 = float(line[2])
                    value = float(line[3])

                    out_string += str(pca_1) + " " + str(pca_2) + "\n"
                except ValueError:
                    pass

    with open(args.pca_out, 'w') as o:
        o.write(out_string)


if __name__ == '__main__':
    main(sys.argv)