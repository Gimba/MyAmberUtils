import sys
import argparse
import re


def reindex_ABC_residues(lst):
    clean_list = []
    index_increment = 0
    for k in lst:
        if k.isdecimal():
            clean_list.append(int(k) + index_increment)

        else:
            index_increment += 1
            res_id = int(re.findall(r'\d+', k)[0]) + index_increment
            clean_list.append(res_id)
    return clean_list


def main(args):
    parser = argparse.ArgumentParser(description='Resolve issues with pdb numbering.')
    parser.add_argument('pdb_file', help='pdb_file')
    args = parser.parse_args()


if __name__ == '__main__':
    main(sys.argv)
