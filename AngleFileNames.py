import CalcResNum1iqd as cr

out = ""
for a in ["phi","psi","chip"]:
    for i in range(1,584):
        res_type = cr.convert(i)
        if res_type:
            a_temp = a
            if a == "chip":
                a_temp = "chi1"
            out += "multidihedral " + a + " resrange " + str(i) +" out angles/" + a_temp + res_type.split()[-1]\
                   + \
                                                                                       ".xvg\n"

with open("all_phi_psi_chi1.cpptraj","w") as o:
    o.write(out)