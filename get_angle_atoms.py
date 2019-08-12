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
    parser = argparse.ArgumentParser(description='Return atom-numbers belonging to angle of residue')
    parser.add_argument('pdb', help='pdb file')
    parser.add_argument('angle', help='e.g. phi, psi')
    parser.add_argument('residue', help='residue')
    args = parser.parse_args()

    residue = int(args.residue)
    with open(args.pdb, 'r') as f:

        # store previous and next residue as well
        residues = {}
        for line in f.readlines():
            if 'ATOM' in line[:4] and not 'WAT'in line[17:22]:
                line_res = int(line[20:28])
                if residue-1 <= line_res and residue+1 >= line_res:
                    residues[str(line_res) + line[12:17].strip()] = int(line[5:12])

    if args.angle == 'psi':
        out = [residues[str(residue) + 'N'], residues[str(residue) + 'CA'], residues[str(residue) + 'C'],
                                                      residues[str(residue+1) + 'N']]
    elif args.angle == 'phi':
        out = [residues[str(residue-1) + 'C'], residues[str(residue) + 'N'], residues[str(residue) + 'CA'],
               residues[str(residue) + 'C']]
    out.sort()
    print(str(out).replace(" ","")[1:-1])


if __name__ == '__main__':
    main(sys.argv)