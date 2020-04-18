import sys
import argparse


def main(args):
    parser = argparse.ArgumentParser(description='Resolve issues with pdb numbering.')
    parser.add_argument('pdb_file', help='pdb_file')
    args = parser.parse_args()


if __name__ == '__main__':
    main(sys.argv)
