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
import numpy as np

__author__ = 'Martin Rosellen'
__docformat__ = "restructuredtext en"

def main(argv):
    parser = argparse.ArgumentParser(description='')

    parser.add_argument('e_dist_data', help='Contacts file generated')

    args = parser.parse_args()

    keys = ["energy", "42-142", "47-142", "77-142", "78-142", "79-142", "80-142", "49-142", "82-142",
            "143-142", "23-142", "24-142", "25-142", "26-142", "27-142", "50-142", "142-42", " 47-42",
            " 77-42", " 78-42", " 79-42", " 80-42", " 49-42", " 82-42", "143-42", " 23-42", " 24-42",
            " 25-42", " 26-42", " 27-42", " 50-42", "142-47", " 42-47", " 77-47", " 78-47", " 79-47",
            " 80-47", " 49-47", " 82-47", "143-47", " 23-47", " 24-47", " 25-47", " 26-47", " 27-47",
            " 50-47", "142-77", " 42-77", " 47-77", " 78-77", " 79-77", " 80-77", " 49-77", " 82-77",
            "143-77", " 23-77", " 24-77", " 25-77", " 26-77", " 27-77", " 50-77", "142-78", " 42-78",
            " 47-78", " 77-78", " 79-78", " 80-78", " 49-78", " 82-78", "143-78", " 23-78", " 24-78",
            " 25-78", " 26-78", " 27-78", " 50-78", "142-79", " 42-79", " 47-79", " 77-79", " 78-79",
            " 80-79", " 49-79", " 82-79", "143-79", " 23-79", " 24-79", " 25-79", " 26-79", " 27-79",
            " 50-79", "142-80", " 42-80", " 47-80", " 77-80", " 78-80", " 79-80", " 49-80", " 82-80",
            "143-80", " 23-80", " 24-80", " 25-80", " 26-80", " 27-80", " 50-80", "142-49", " 42-49",
            " 47-49", " 77-49", " 78-49", " 79-49", " 80-49", " 82-49", "143-49", " 23-49", " 24-49",
            " 25-49", " 26-49", " 27-49", " 50-49", "142-82", " 42-82", " 47-82", " 77-82", " 78-82",
            " 79-82", " 80-82", " 49-82", "143-82", " 23-82", " 24-82", " 25-82", " 26-82", " 27-82",
            " 50-82", " 142-143", "42-143", "47-143", "77-143", "78-143", "79-143", "80-143", "49-143",
            "82-143", "23-143", "24-143", "25-143", "26-143", "27-143", "50-143", "142-23", " 42-23",
            " 47-23", " 77-23", " 78-23", " 79-23", " 80-23", " 49-23", " 82-23", "143-23", " 24-23",
            " 25-23", " 26-23", " 27-23", " 50-23", "142-24", " 42-24", " 47-24", " 77-24", " 78-24",
            " 79-24", " 80-24", " 49-24", " 82-24", "143-24", " 23-24", " 25-24", " 26-24", " 27-24",
            " 50-24", "142-25", " 42-25", " 47-25", " 77-25", " 78-25", " 79-25", " 80-25", " 49-25",
            " 82-25", "143-25", " 23-25", " 24-25", " 26-25", " 27-25", " 50-25", "142-26", " 42-26",
            " 47-26", " 77-26", " 78-26", " 79-26", " 80-26", " 49-26", " 82-26", "143-26", " 23-26",
            " 24-26", " 25-26", " 27-26", " 50-26", "142-27", " 42-27", " 47-27", " 77-27", " 78-27",
            " 79-27", " 80-27", " 49-27", " 82-27", "143-27", " 23-27", " 24-27", " 25-27", " 26-27",
            " 50-27", "142-50", " 42-50", " 47-50", " 77-50", " 78-50", " 79-50", " 80-50", " 49-50",
            " 82-50", "143-50", " 23-50", " 24-50", " 25-50", " 26-50", " 27-50"]
    keys = [item.strip() for item in keys]

    with open(args.e_dist_data, 'r') as f:
        content = f.read()
        content = content.splitlines()

        content = [item.split() for item in content]

        energies = c_get(content, 0)

        distances = []

        for i in range(1, len(content[0]) - 1):
            distances.append(c_get(content, i))
        corr = []
        for dist in distances:
            corr.append(np.corrcoef(energies, dist)[1, 0])

        corr_dict = {}

        for i in range(len(distances)):
            corr_dict[keys[i+1]] = corr[i]

        max_corr = max(corr_dict, key=corr_dict.get)
        min_corr = min(corr_dict, key=corr_dict.get)
        print(max_corr, corr_dict[max_corr])
        print(min_corr, corr_dict[min_corr])

        import operator

        sorted_x = sorted(corr_dict.items(), key=operator.itemgetter(1))

        print sorted_x

def c_get(lst, column):
    outlist = []
    for item in lst:
        outlist.append(item[column])
    return outlist

if __name__ == "__main__":
    main(sys.argv)

