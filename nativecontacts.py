#! /usr/bin/env python

import sys
import argparse
import glob
import pytraj as pt

def main(argv):
    parser = argparse.ArgumentParser(description='Calculates the contacts of the given masks')
    parser.add_argument('prmtop', help='prmtop')
    p