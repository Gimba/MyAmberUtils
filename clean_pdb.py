import sys
import argparse
import re


def reindex_ABC_residues(lst):
    clean_list = []
    index_increment = 0
    for k in lst:
        k = k.strip()
        if k.isdecimal():
            clean_list.append(int(k) + index_increment)

        else:
            index_increment += 1
            res_id = int(re.findall(r'\d+', k)[0])
            res_id_new = res_id + index_increment
            print('replaced',k,'with',res_id_new)
            clean_list.append(res_id)
    return clean_list


def main(args):
    parser = argparse.ArgumentParser(description='Resolve issues with pdb numbering.')
    parser.add_argument('pdb_file', help='pdb_file')
    args = parser.parse_args()

    file = args.pdb_file
    residues = {}
    # seqres = {}
    with open(file, 'r') as f:
        for line in f.readlines():
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


if __name__ == '__main__':
    main(sys.argv)
