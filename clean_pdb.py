import sys
import argparse
import re


def reindex_ABC_residues(dct):
    mapping = {}

    for k, v in dct.items():
        index_increment = 0
        for res in v:
            res = res.strip()
            if res.isdecimal():
                mapping[str(k) + str(res)] = int(res) + index_increment
            else:
                index_increment += 1
                res_id = int(re.findall(r'\d+', res)[0])
                res_id_new = res_id + index_increment
                print('replaced', res, 'with', res_id_new)
                mapping[str(k) + str(res)] = res_id_new
    return mapping


def main(args):
    parser = argparse.ArgumentParser(description='Resolve issues with pdb numbering.')
    parser.add_argument('pdb_file', help='pdb_file')
    args = parser.parse_args()

    file = args.pdb_file
    residues = {}
    # seqres = {}
    out = []
    with open(file, 'r') as f:
        for line in f.readlines():
            out.append(line)
            # if line[:6] == 'SEQRES':
            #     line = line.split()
            #     if line[2] in seqres.keys():
            #         seqres[line[2]].extend(line[4:])
            #     else:
            #         seqres[line[2]] = line[4:]

            if line[:4] == 'ATOM':
                if line[21] in residues.keys():
                    residues[line[21]].extend([line[22:27]])
                else:
                    residues[line[21]] = [line[22:27]]

    for k, v in residues.items():
        v = list(set(v))
        v = sorted(v, key=lambda x: (int(x[:-1]), x[-1]))
        residues[k] = v

    mapping = reindex_ABC_residues(residues)

    new_out = ''
    with open(file.split('.')[0] + '_cleaned.pdb', 'w') as o:
        outer_counter = 0
        for lo in out:
            if lo[:4] == 'ATOM':
                residue = lo[22:27].strip()
                chain = lo[21]
                mapping_key = chain + residue
                new_resid = str(mapping[mapping_key]).rjust(4) + ' '

                new_out += lo[:22] + new_resid + lo[27:]

                outer_counter += 1
            else:
                new_out += lo

        o.write(new_out)


if __name__ == '__main__':
    main(sys.argv)
