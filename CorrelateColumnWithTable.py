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
    parser = argparse.ArgumentParser(description='Calculates the pearson correlation of a given column (column_file) '
                                                 'with the columns of a table (table_file). It is expected that the '
                                                 'first column of both files is contains titles. The first row of the'
                                                 'table must also contain titles.')
    parser.add_argument('column_file', help='example row: F2196A -96.03)')
    parser.add_argument('table_file', help='example first line: title P09 C22 K53 / second line example: F2196A 4.3 '
                                           '5.1 5.5')
    parser.add_argument('outfile', help='output file')

    args = parser.parse_args()

    column_file = args.column_file
    table_file = args.table_file
    outfile = args.outfile

    column_dict = {}

    with open(column_file, 'r') as c:
        content = c.readlines()

        for line in content:
            temp = line.split()
            column_dict[temp[0]] = temp[1]

    table_dict = {}
    with open(table_file, 'r') as t:
        content = t.readlines()

        for line in content:
            temp = line.split()
            table_dict[temp[0]] = temp [1:]

if __name__ == "__main__":
    main(sys.argv)