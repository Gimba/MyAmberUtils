#! /usr/bin/env python

# Copyright (c) 2020 Martin Rosellen

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

__author__ = 'Martin Rosellen'
__docformat__ = "restructuredtext en"

import sys
import argparse
import pytraj as pt
import numpy as np
from Bio import pairwise2
from modeller import *
import re

res_codes = {}
res_codes['ALA'] = 'A'
res_codes['ARG'] = 'R'
res_codes['ASN'] = 'N'
res_codes['ASP'] = 'D'
res_codes['CYS'] = 'C'
res_codes['CYX'] = 'C'
res_codes['GLU'] = 'E'
res_codes['GLN'] = 'Q'
res_codes['GLY'] = 'G'
res_codes['HIS'] = 'H'
res_codes['HIE'] = 'H'
res_codes['HID'] = 'H'
res_codes['HIP'] = 'H'
res_codes['ILE'] = 'I'
res_codes['LEU'] = 'L'
res_codes['LYS'] = 'K'
res_codes['MET'] = 'M'
res_codes['PHE'] = 'F'
res_codes['PRO'] = 'P'
res_codes['SER'] = 'S'
res_codes['THR'] = 'T'
res_codes['TRP'] = 'W'
res_codes['TYR'] = 'Y'
res_codes['VAL'] = 'V'


def missing_elements(L):
    start, end = L[0], L[-1]
    return sorted(set(range(start, end + 1)).difference(L))


def main(args):
    parser = argparse.ArgumentParser(description='Insert missing residue coordinates using Modeller')
    parser.add_argument('pdb_file', help='pdb_file with missing residues')
    args = parser.parse_args()

    file = args.pdb_file

    residues = {}
    seqres = {}
    last_res = 0
    with open(file, 'r') as f:
        for line in f.readlines():
            if line[:6] == 'SEQRES':
                line = line.split()
                if line[2] in seqres.keys():
                    seqres[line[2]].extend(line[4:])
                else:
                    seqres[line[2]] = line[4:]

            if line[:4] == 'ATOM':
                res_num = int(line[22:27])
                if last_res != res_num:
                    if line[21] in residues.keys():
                        residues[line[21]].extend([line[17:20]])
                    else:
                        residues[line[21]] = [line[17:20]]
                    last_res = res_num

    sequence_with_gaps = ''
    fill = ''
    for chain in seqres.keys():
        seqres_code = ''.join([res_codes[rc1] for rc1 in seqres[chain]])
        seqres_code += '/'
        res_code = ''.join([res_codes[rc2] for rc2 in residues[chain]])
        res_code += '/'
        alignments = pairwise2.align.globalxx(seqres_code, res_code)
        sequence_with_gaps += alignments[0][1]
        fill += seqres_code

    # add line breaks after 75 characters
    sequence_with_gaps = re.sub("(.{75})", "\\1\n", sequence_with_gaps, 0, re.DOTALL)
    fill = re.sub("(.{75})", "\\1\n", fill, 0, re.DOTALL)

    # Get the sequence of the 1qg8 PDB file, and write to an alignment file
    code = file

    e = environ()
    m = model(e, file=code)
    aln = alignment(e)
    aln.append_model(m, align_codes=code)
    aln.write(file=code + '.seq')

    ## modeller does some reordering of the chains which is not optimal if we want to do an alignment
    # seqres_modeller = ''
    # with open(code + '.seq') as k:
    #     for line in k.readlines()[3:]:
    #         seqres_modeller += line.strip('\n')

    # extract header from modeller sequence file
    out = ''
    header = []
    with open(code + '.seq') as k:
        for line in k.readlines()[:3]:
            header.append(line)

    out += ''.join(header)
    out += sequence_with_gaps[:-1] + '*\n'
    out += "\n\n"
    out += header[1].strip('\n') + '-fill\n'
    out += 'sequence:::::::::\n'
    out += fill[:-1] + '*\n'

    with open(file + '.ali', 'w') as o:
        o.write(out)


if __name__ == '__main__':
    main(sys.argv)
