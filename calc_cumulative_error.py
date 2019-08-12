#! /usr/bin/env python

import argparse
import sys
from math import sqrt,pow,fabs
from kd2ddG import kd2ddg

def my_number_to_float(input_number):
    if '*' in input_number:
        number, exponent = input_number.split('*')
        base, exponent = exponent.split('^')
        number = float(number)*(pow(float(base),float(exponent)))
    else:
        number = float(input_number)
    return number

def main(argv):
    parser = argparse.ArgumentParser(description='Calculate cumulative error.')
    parser.add_argument('R', help='value of combined values')
    parser.add_argument('X', help='first value')
    parser.add_argument('dX', help='error of first value')
    parser.add_argument('Y', help='second value')
    parser.add_argument('dY', help='error of second value')

    args = vars(parser.parse_args())

    for k,v in args.items():
        args[k] = my_number_to_float(v)


    R, X, dX, Y, dY = args['R'], args['X'], args['dX'], args['Y'], args['dY']

    KD = Y/X

    rms_percentage =  sqrt(pow(dX/X,2) + pow(dY/Y,2))

    KD_error = fabs(KD) * rms_percentage

    ddG = kd2ddg(KD, 298.15)

    ddG_error = ddG * rms_percentage

    print(ddG, KD, ddG_error, KD_error)


if __name__ == '__main__':
    main(sys.argv)