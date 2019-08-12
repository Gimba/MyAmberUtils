# #!/usr/bin/perl -w
# ! /usr/bin/env python

# Copyright (c) 2018 Martin Rosellen

# Permission is hereby granted, free of charge, to any person obtaining a
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys, argparse
import re
from os.path import basename
import pytraj as pt


def main(args):
    parser = argparse.ArgumentParser(description='Prepare config files for umbrella sampling run.')
    parser.add_argument('raf', help='list like: "residues_1,angle_1_from,angle_1_to,force_1:residues_2,angle_2_from,'
                                    'angle_2_to,force_2:..."')
    parser.add_argument('umbrellas', help='how many umbrella do we want to span?')
    parser.add_argument('init', help='names of initial structures, e.g. "rel_3.rst,prod_1.rst"')
    parser.add_argument('-s', action='store_true',
                        help='define weather the last frame of each simulation is used for the next one as a start. '
                             'In this case there should be only one init file')
    args = parser.parse_args()

    pdb = pt.load('R2220Q.inpcrd', 'R2220Q.prmtop')

    umbrellas = int(args.umbrellas)
    configs_directory = "umbrella_config/"

    # there is possibly more than one angle that gets transformed
    residues_angles_force = args.raf.split('|')

    # angle increments contains the step size for every configuration
    angle_increments = []

    # contains [[atom1,atom2,...][angle1,angle2][force]]
    umbrella_configs = []

    # read input arguments into variables
    for cnfg_arguments in residues_angles_force:
        cnfg_arguments = re.sub('\'|\"', '', cnfg_arguments)

        residues, angles, force = cnfg_arguments.split(':')
        angles = angles.split(',')
        angles = list(map(float, angles))
        print(residues)
        atoms = [str(pt.select_atoms(':' + k + '@CA', pdb.top)[0]) for k in residues.split(',')]
        print(atoms)
        umbrella_config = []
        umbrella_config.append(atoms)
        umbrella_config.append(angles)
        umbrella_config.append(force)
        umbrella_configs.append(umbrella_config)

        angle_increments.append(abs(umbrella_config[1][0] - umbrella_config[1][1]) / umbrellas)

    umbrella_constraint_files = []
    n_cnfgs = len(umbrella_configs)

    # create dictionary to hold meta files
    meta_files = {}
    for n in range(n_cnfgs):
        meta_files[n] = ""

    # generate meta files and umbrella contstraint files umb_out_...dat
    meta_out = ""
    for c in range(umbrellas + 1):
        out = "Harmonic restraints\n"
        for i in range(n_cnfgs):

            out += " &rst\n"

            residues = umbrella_configs[i][0]
            out += "  iat=" + ','.join(atoms) + ",\n"

            angle_low_bound = umbrella_configs[i][1][0] - 180
            angle = umbrella_configs[i][1][0]
            angle_high_bound = umbrella_configs[i][1][0] + 180
            out += "  r1={}, r2={}, r3={}, r4={}\n".format(angle_low_bound, angle, angle, angle_high_bound)

            force = umbrella_configs[i][2]
            out += "  rk2={}, rk3={}\n/\n".format(force, force)

            meta_out += '../umbrella_productions/prod_25C_{}.dat {} 0.12184\n'.format(c, angle)

            if angles[0] > angles[1]:
                umbrella_configs[i][1][0] -= angle_increments[i]
            else:
                umbrella_configs[i][1][0] += angle_increments[i]

        umbrella_constraint_file_name = '{}umb_out_{}.dat'.format(configs_directory, c)
        with open(umbrella_constraint_file_name, 'w') as f:
            f.write(out)
        umbrella_constraint_files.append(umbrella_constraint_file_name)

    # write meta file
    print(meta_out)
    with open(configs_directory + 'meta_file', 'w') as mf:
        mf.write(meta_out)

    ## generate simulation configurations with umbrella constraints

    # initial/template configuration files
    sim_configuration_files = ['../min_1.umbin',
                               '../rel_1.umbin',
                               '../rel_2_25C.umbin',
                               '../rel_3_25C.umbin',
                               '../prod_25C.umbin']

    md_files = []
    for init_f in sim_configuration_files:

        with open(init_f, 'r') as m:
            sim_config_content = m.readlines()

        # add umbrella constraints to simulation configuration
        for i, f in enumerate(umbrella_constraint_files):

            if "prod_25C" in init_f:

                # remove the last two lines
                md_in_temp = "".join(sim_config_content[:-2])

                # add contraints
                md_in_temp += "DISANG=./{}\n".format(f)
                # add meta data file name
                md_in_temp += "DUMPAVE=./umbrella_productions/prod_25C_{}.dat\n".format(i)

            else:
                md_in_temp = "".join(sim_config_content[:-1])
                md_in_temp += "DISANG=./{}\n".format(f)

            # write simulation configuration file
            sim_file_name = basename(init_f).split('.')
            with open(configs_directory + sim_file_name[0] + "_" + str(i) + "." + sim_file_name[1], 'w') as o:
                o.write(md_in_temp)
                md_files.append(configs_directory + sim_file_name[0] + "_" + str(i) + "." + sim_file_name[1])

    ## generate run scripts

    init_files = args.init.split(',')
    if args.s and len(init_files) > 1:
        print("too many input files for option s. Exiting.")
        exit()

    runs_per_script = umbrellas // len(init_files)
    umbrellas = umbrellas + 1
    idx = 0
    for init_f in init_files:
        out = ""
        while idx <= runs_per_script and idx <= umbrellas and idx + umbrellas * 4 < len(md_files):
            b_name_min = basename(md_files[idx]).split('.')[0]
            run_min = \
                "pmemd -O " \
                "-i {} " \
                "-o umbrella_productions/{}.out " \
                "-p WT.prmtop " \
                "-c {} " \
                "-r umbrella_productions/{}.rst " \
                "-inf umbrella_productions/{}.mdinfo \n" \
                    .format(md_files[idx], b_name_min, init_f, b_name_min, b_name_min)

            b_name_rel_1 = basename(md_files[idx + umbrellas]).split('.')[0]
            run_rel_1 = \
                "pmemd.cuda -O " \
                "-i {} " \
                "-o umbrella_productions/{}.out " \
                "-p WT.prmtop " \
                "-c umbrella_productions/{}.rst " \
                "-r umbrella_productions/{}.rst " \
                "-inf umbrella_productions/{}.mdinfo " \
                "-ref umbrella_productions/{}.rst \n" \
                    .format(md_files[idx + umbrellas], b_name_rel_1, b_name_min, b_name_rel_1, b_name_rel_1, b_name_min)

            b_name_rel_2 = basename(md_files[idx + umbrellas * 2]).split('.')[0]
            run_rel_2 = \
                "pmemd.cuda -O " \
                "-i {} " \
                "-o umbrella_productions/{}.out " \
                "-p WT.prmtop " \
                "-c umbrella_productions/{}.rst " \
                "-r umbrella_productions/{}.rst " \
                "-inf umbrella_productions/{}.mdinfo " \
                "-ref umbrella_productions/{}.rst \n" \
                    .format(md_files[idx + umbrellas * 2], b_name_rel_2, b_name_rel_1, b_name_rel_2, b_name_rel_2,
                            b_name_rel_1)

            b_name_rel_3 = basename(md_files[idx + umbrellas * 3]).split('.')[0]
            run_rel_3 = \
                "pmemd.cuda -O " \
                "-i {} " \
                "-o umbrella_productions/{}.out " \
                "-p WT.prmtop " \
                "-c umbrella_productions/{}.rst " \
                "-r umbrella_productions/{}.rst " \
                "-inf umbrella_productions/{}.mdinfo " \
                "-ref umbrella_productions/{}.rst \n" \
                    .format(md_files[idx + umbrellas * 3], b_name_rel_3, b_name_rel_2, b_name_rel_3, b_name_rel_3,
                            b_name_rel_2)

            b_name_prod = basename(md_files[idx + umbrellas * 4]).split('.')[0]
            run_prod = \
                "pmemd.cuda -O " \
                "-i {} " \
                "-o umbrella_productions/{}.out " \
                "-p WT.prmtop " \
                "-c umbrella_productions/{}.rst " \
                "-r umbrella_productions/{}.rst " \
                "-inf umbrella_productions/{}.mdinfo " \
                "-x umbrella_productions/{}.nc " \
                "-ref umbrella_productions/{}.rst \n" \
                    .format(md_files[idx + umbrellas * 4], b_name_prod, b_name_rel_3, b_name_prod, b_name_prod,
                            b_name_prod, \
                            b_name_rel_3)

            out += "#{}\n".format(idx)
            idx += 1
            out += run_min + "\n" + run_rel_1 + "\n" + run_rel_2 + "\n" + run_rel_3 + "\n" + run_prod + "\n"

            if args.s:
                init_f = "umbrella_productions/" + b_name_prod + ".rst"

        # write run script
        if args.s:
            script_file_name = 'init_WT_run_s_' + str(idx) + ".sh"

        else:
            script_file_name = 'init_' + basename(init_f).split('.')[0] + "_run_" + str(idx) + ".sh"

        print(script_file_name)
        with open(script_file_name, "w") as o:
            o.write("#!/bin/bash\n\n")
            o.write(out)
        print(runs_per_script)
        runs_per_script *= 2


if __name__ == '__main__':
    main(sys.argv)
