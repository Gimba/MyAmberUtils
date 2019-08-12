

def main():
    with open("FINAL_DECOMP_MMPBSA_table_WT.csv", 'r') as f:
        lines = f.readlines()
        residues = lines[0].split(',')[1:]

        print(residues)

        row_res = {}
        out = ""
        for line in lines[1:]:
            line = line.split(',')

            indexes = [i for i, e in enumerate(line[1:-1]) if e != '']
            if indexes:
                temp_lst = []
                for idx in indexes:
                    temp_lst.append(residues[idx+1])
                    # print(line[idx+1])
                    # print(line[0])
                    res1 = line[0].split()[1]
                    res2 = residues[idx].split()[1]
                    out += "distance :{}@CA :{}@CA {}<->{} out distances.dat\n".format(res1, res2, res1,res2)
                row_res[line[0]] = temp_lst
            # print(row_res)
            # if count > 10:
            #     exit()
        with open("distance.in", 'w') as o:
            o.write(out)

if __name__ == '__main__':
    main()