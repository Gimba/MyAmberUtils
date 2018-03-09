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

import sys
import argparse
import os
from collections import defaultdict
from collections import OrderedDict
import re
from scipy.stats.stats import pearsonr

__author__ = 'Martin Rosellen'
__docformat__ = "restructuredtext en"

def main(argv):
    parser = argparse.ArgumentParser(description='Create a file containing all the calculated energy values.')
    parser.add_argument('file_ending', help='name endings of files containing angle values, e.g. standard deviation ('
                                            'example: "sum.txt"')
    parser.add_argument('outfile', help='output file')

    args = parser.parse_args()
    energy_files = []

    file_ends = args.file_ending

    for root, dirs, files in os.walk("."):
        for name in files:
            if name.endswith(file_ends) and len(root.split("/")) == 5:
                energy_files.append(str(os.path.join(root, name)))
    energies = defaultdict(list)
    energy_files.sort()

    out = ""

    for file in energy_files:
        with open (file, 'r') as f:
            content = f.readlines()
            out += file.split("/")[1] + " " + content[-1][9:]


    with open(args.outfile, 'w') as o:
        o.write(out)

if __name__ == "__main__":
    main(sys.argv)