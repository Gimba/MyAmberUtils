#! /usr/bin/env python

# -*- coding: utf-8 -*-

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


import sys
import argparse

def main(argv):
    parser = argparse.ArgumentParser(description='Exchange the residue numbers in the given file with the ones from the '
                                                 'reference mapping. The regex further restricts replacing positions')
    parser.add_argument('file', help='data where residue numbers should be exchanged')
    parser.add_argument('mapping', help='residue number mapping file')
    parser.add_argument('regex', help='regular expression that tells where residues can be found.')
    args = parser.parse_args()

    regex = args.regex

    mapping = args.mapping

    file = args.file


    mappings = {}
    with open(mapping, 'r') as f:
        content = f.readlines()
        for line in content:
            if len(line) > 1:
                temp = line.split()
                mappings[temp[0]] = temp[1]

if __name__ == "__main__":
    main(sys.argv)
