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

from scipy.stats.stats import pearsonr

import ListHelper as lh

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

    table_dict = {}
    with open(table_file, 'r') as t:
        content = t.readlines()

        # first row specifies column headers
        column_headers = content[0].split()

        # add values to row headers
        for line in content[1:]:
            temp = line.split()
            table_dict[temp[0]] = temp [1:]

    # append data from column file using the keys specified in the first column
    with open(column_file, 'r') as c:
        content = c.readlines()

        for line in content:
            temp = line.split()
            if temp[0] in table_dict.keys():
                table_dict[temp[0]].append(temp[1])

    # sort out table rows that have no corresponding row in column file
    last = table_dict.items()[0]
    for item in table_dict.items():
        if len(item[1]) > len(last[1]):
            table_dict.pop(last[0])
            last = item

        elif len(item[1]) < len(last[1]):
            table_dict.pop(item[0])

    # convert dictionnary values to 2D list(table)
    table = lh.dict_to_2D_list(table_dict)
    table = [[float(i) for i in nested] for nested in table]

    # extract master column (the column we want to correlate all other columns with)
    master_column = lh.c_get(table, -1)

    out = "residue\tr-value\tp-value\n"
    # calculate correlations
    for i in range(len(table[0])-1):
        selected_column = lh.c_get(table, i)

        # check if column only contains 0s (this can happen when the only entry that contains a value other than 0 gets
        # removed from the dictionnary in the 'sort out table rows that have no corresponding ...' step)
        if all(p == 0.0 for p in selected_column):
            continue

        corr = pearsonr(master_column, selected_column)

        out += column_headers[i+1] + "\t" + str(round(corr[0],2)) + "\t" + str(round(corr[1],2)) + "\n"

    with open(outfile, 'w') as o:
        o.writelines(out)


if __name__ == "__main__":
    main(sys.argv)
