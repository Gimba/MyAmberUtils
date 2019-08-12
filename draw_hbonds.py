import sys
import csv
import numpy as np
import DrawInteractions as di

def get_resnum(r):
    r_temp = r.split('@')
    r_atom = r_temp[1]
    r_type, r_num = r_temp[0].split("_")
    return r_num, r_type, r_atom

def draw_interactions(file_name, thres = 150):

    out = ""
    with open(file_name, 'r') as f:
        acceptors = {}
        for line in f:
            if '@' in line:
                (acceptor, hdonor, donor, frames, frac, avgdist, avgang) = line.split()
                frames = int(frames)
                if acceptor.split('@')[1][0] != 'H' and donor.split('@')[1][0] != 'H':
                    if frames > thres:
                        acceptors[acceptor] = [donor, frames]

        for k, v in acceptors.items():
            a_num, a_type, a_atom = get_resnum(k)
            d_num, d_type, d_atom = get_resnum(v[0])
            out += "show lines,(resi " + a_num + ")" + "\n"
            out += "show lines,(resi " + d_num + ")" + "\n"
            out += "bond resi " + a_num + " and resn " + a_type + " and name " + a_atom + ", resi " + d_num + " and " \
            "resn " +  d_type + " and name " + d_atom + "\n"

            gb = str(200 / v[1] - 1)
            c_name = (k + v[0]).replace('@', '')

            out += "set_color " + c_name + " = [1.0, " + gb + "," + gb + "]" + "\n"
            out += "set_bond line_color, " + c_name + ", resi " + a_num + " and resn " + a_type + " and name " + \
                   a_atom + ", resi " + d_num + " and resn " + d_type + " and name " + d_atom + "\n"
            out += "set_bond line_width, " + str(5) + ", resi " + a_num + " and resn " + a_type + " and name " + \
                  a_atom + ", resi " + d_num + " and resn " + d_type + " and name " + d_atom + "\n"
    return out

# with open('AV_HBOND_ACCEPTORS_prod4.dat', 'r') as f, open('AV_HBOND_DONORS_prod4.dat', 'r') as g:
#     thres = 100
#     out = ""
#     acceptors = {}
#     for line in f:
#         if '@' in line:
#             (acceptor, hdonor, donor, frames, frac, avgdist, avgang) = line.split()
#             frames = int(frames)
#             if acceptor.split('@')[1][0] != 'H' and donor.split('@')[1][0] != 'H':
#                 if frames > thres:
#                     acceptors[acceptor] = [donor, frames]
#
#     print("set line_width, 5")
#     print("set ray_opaque_background, on")
#     print("set cartoon_gap_cutoff, 0")
#
#     for k,v in acceptors.items():
#         a_num, a_type, a_atom = get_resnum(k)
#         d_num, d_type, d_atom = get_resnum(v[0])
#         print("show lines,(resi " + a_num + ")")
#         print("show lines,(resi " + d_num + ")")
#         print("bond resi " + a_num + " and resn " + a_type + " and name " + a_atom +", resi " + d_num + " and "
#                                                                                                         "resn " +
#               d_type + " and name " + d_atom)
#         gb = str(200/v[1] - 1)
#         c_name = (k + v[0]).replace('@','')
#         print("set_color " + c_name + " = [1.0, " + gb + "," + gb +"]")
#         print("set_bond line_color, " + c_name + ", resi " + a_num + " and resn " + a_type + " and name " + a_atom
#               + ", "
#                 "resi " + d_num + " "
#                                   "and "
#                                   "resn " +
#               d_type + " and name " + d_atom)
#         print("set_bond line_width, " + str(5) + ", resi " + a_num + " and resn " + a_type + " and name " +
#               a_atom
#               + ", "
#                 "resi " + d_num + " "
#                                   "and "
#                                   "resn " +
#               d_type + " and name " + d_atom)
#
#
#
#
#     donors = {}
#     for line in g:
#         if '@' in line:
#             (acceptor, hdonor, donor, frames, frac, avgdist, avgang) = line.split()
#             frames = int(frames)
#             if acceptor.split('@')[1][0] != 'H' and donor.split('@')[1][0] != 'H':
#                 if frames > thres:
#                     donors[acceptor] = [donor, frames]
#
#
#     print('ray')

def main(args):
    pymol = ""
    pymol += "set line_width, 5\n"
    pymol += "bg_color, white\n"
    pymol += "set ray_opaque_background, on\n"
    pymol += "set cartoon_gap_cutoff, 0\n"
    pymol += draw_interactions("AV_HBOND_ACCEPTORS_prod4.dat")
    pymol += draw_interactions("AV_HBOND_DONORS_prod4.dat")
    pymol += "\nray"
    with open("draw_hbond_interactions.pymol", "w") as o:
        o.write(pymol)

    # cols = {}
    # residue_ids = []
    # col_ids = []
    # di.read_control_file("1iqd_interactions_control.csv", col_ids, cols, residue_ids)
    #
    # energies = {}
    # res_with_energy = []
    # di.read_decomp_file("FINAL_DECOMP_MMPBSA_table.csv", energies, res_with_energy, residue_ids, 0)
    #
    #
    # for v in energies.values():
    #     print(v)
    #     res_0 = v.split()
    #     print("bond resi " + v[0] + " and resn ASP and name OD1, resi 79 and resn LEU and name N")

if __name__ == '__main__':
    main(sys.argv)