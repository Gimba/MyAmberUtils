#! /usr/bin/env python

# Copyright (c) 2019 Martin Rosellen

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
import pytraj as pt

def main(argv):
    parser = argparse.ArgumentParser(description='Script to check for hydrogen binding between watermolecules between 2 given residue masks.')
    parser.add_argument('parm', help='parm file')
    parser.add_argument('trajin', help='trajectory')
    parser.add_argument('mask1', help='mask 1')
    parser.add_argument('mask2', help='mask 2')

    args = parser.parse_args()
    traj = pt.iterload(args.trajin, args.parm)
    # print(traj)
    #
    # traj = pt.datafiles.load_tz2_ortho()
    # print(traj)
    # print(pt.native_contacts(traj, mask=':42', include_solvent=True))
    print(pt.native_contacts(traj, mask=':42', mask2=":WAT", distance=1.0, include_solvent=True))
    # print(water_contacts)


if __name__ == '__main__':
    main(sys.argv)