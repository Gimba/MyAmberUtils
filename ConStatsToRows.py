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

# This program is intended to replace specified residues with those generated from a modeller run.
# imported atom numbers are set to zero, to avoid conflicts with CONECT records in the original file.

__author__ = 'Martin Rosellen'
__docformat__ = "restructuredtext en"

import sys
import os
from collections import defaultdict


def main(argv):

    file_ends = "guani_47_stat.dat"
    contact_files = []
    order = []

    for root, dirs, files in os.walk("."):
        for name in files:
            if name.endswith(file_ends):
                contact_files.append(str(os.path.join(root, name)))
                order.append(name.split("_")[0])

    contact_files.sort()
    order.sort()

    contacts = []

    for file in contact_files:
        with open(file, 'r') as f:
            content = f.readlines()

            for i in range(1,len(content)):
                contacts.append(content[i].split()[1])

    contacts = list(set(contacts))

    resorted = {}

    for item in contacts:
        resorted[item] = [0]*len(order)


    n = 0
    for fl in contact_files:
        with open(fl, 'r') as f:
            content = f.readlines()

            for l in content[1:]:
                temp = l.split()
                res = temp[1]
                cnt = temp[3]
                # print(resorted[res][n])
                resorted[res][n] = cnt
        n += 1

    out = [[0] + order]


    for key, value in resorted.items():
        out.append([key] + value)

    print(out)

    out = list(map(list, zip(*out)))

    print(out)

if __name__ == "__main__":
    main(sys.argv)
