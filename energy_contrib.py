#! /usr/bin/env python

import pandas as pd
from os import listdir
import re

def main():
    csv_cmp_file = [f for f in listdir(".") if "cmp.csv" in f]
    if not csv_cmp_file:
        return
    data = pd.read_csv(csv_cmp_file[0])
    energy_total = sum(data[data['Chain'] == 'C']['Total'])
    res_id = re.findall(r'\d+', csv_cmp_file[0])[0]
    mutation_energy = float(data[data['Residue'].str.contains(res_id)]['Total'])

    with open(csv_cmp_file[0].split('.')[0] + "_ratio.csv", 'w') as o:
        o.write(csv_cmp_file[0].split('_')[0] + "," + str(energy_total) + "," + str(mutation_energy))

if __name__ == '__main__':
    main()