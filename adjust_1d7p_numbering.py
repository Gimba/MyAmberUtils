#! /usr/bin/env python

import argparse
import sys

def main(argv):
    parser = argparse.ArgumentParser(description='Adjust the residue numbering of 1d7p')
    parser.add_argument('file', help='infile')
    parser.add_argument('output', help='output file name')
    args = parser.parse_args()

    with open(args.file, 'r') as f:

        temp = []
        first_atom = None

        for line in f:
            if 'ATOM' in line:
                if int(line[21:27].strip()) > 3:
                    if not first_atom:
                        first_atom = int(line[6:12])

                    a = int(line[6:12]) - first_atom + 1
                    a = '{:6.0f}'.format(a)

                    l = int(line[21:27]) - 3
                    l = '{:6.0f}'.format(l)
                    line = line[:5] + a + line[12:20] + l + line[28:]
                    temp.append(line)
            else:
                temp.append(line)
                if 'MODEL' in line:
                    print('{0}\r'.format(line))

        output = temp

    with open(args.output, 'w') as o:
        o.writelines(output)

if __name__ == '__main__':
    main(sys.argv)

