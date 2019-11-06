#! /usr/bin/env python

import sys


def main(args):
    with open("40ns_productions_short/mmpbsa/FINAL_RESULTS_MMPBSA.dat", 'r') as mm:
        with open("40ns_productions_short/decomp/FINAL_RESULTS_MMPBSA.dat", 'r') as decomp:
            with open("40ns_productions_short/decomp_7A/FINAL_RESULTS_MMPBSA.dat", 'r') as decomp_7A:
                content_mm = mm.readlines()
                mm_total = float([c.split()[2] for c in content_mm if 'DELTA TOTAL' in c][0])

                content_decomp = decomp.readlines()
                decomp_total = float([c.split()[2] for c in content_decomp if 'DELTA TOTAL' in c][0])

                content_decomp_7A = decomp_7A.readlines()
                decomp_7A_total = float([c.split()[2] for c in content_decomp_7A if 'DELTA TOTAL' in c][0])

                if abs(mm_total - decomp_7A_total) > 1:
                    print('mm_total - decomp_7A', mm_total - decomp_7A_total)

                if abs(mm_total - decomp_total) > 1:
                    print('mm_total - decomp', mm_total - decomp_total)

                if abs(decomp_total - decomp_7A_total) > 1:
                    print('decomp_total - decomp_7A', decomp_total - decomp_7A_total)


if __name__ == '__main__':
    main(sys.argv)
