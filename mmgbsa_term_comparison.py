import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = (10,8)

def read_mmgbsa_final(file_name):
    out = {}
    headers = ['Complex:','Receptor:','Ligand:']
    with open(file_name, 'r') as f:
        l = 0
        for line in f.readlines()[35:]:
            if l < len(headers) and headers[l] in line:
                h = headers[l]
                l += 1


            line = line.split('  ')
            line = [li for li in line if li]
            # print(line)
            if line:
                if 'DELTA' in line[0]:
                    # print(line)
                    out[line[0]] = line[1]
                elif len(line) > 2 and 'Energy' not in line[0]:
                    out[h + line[0]] = line[1]
    return out


if __name__ == '__main__':
    WT = read_mmgbsa_final("/d/as12/u/rm001/1iqd_data/back_muta/25_Celsius/WT_prod_20/WT/40ns_productions_short"
                       "/mmpbsa/FINAL_RESULTS_MMPBSA.dat")

    mutants = ['WT', 'R2215A', 'R2220A', 'R2220Q', 'F2200A', 'F2196A','M2199A', 'V2223M', 'H2309A']
    mut_data = {}
    mut_diffs = {}
    fig, ax = plt.subplots()
    index = np.arange(len(WT.keys()) + 1)
    bar_width = 1.0/float(len(mutants) + 1)
    cmap = plt.get_cmap('jet')
    colors = [cmap(1. * i / len(mutants)) for i in range(len(mutants))]
    for i,m in enumerate(mutants):

        mut_data[m] = read_mmgbsa_final("/d/as12/u/rm001/1iqd_data/back_muta/25_Celsius/WT_prod_20/" + m +
                                   "/40ns_productions_short"
                           "/mmpbsa/FINAL_RESULTS_MMPBSA.dat")
    means = dict.fromkeys(mut_data[mutants[0]].keys(), 0.0)

    for k,m in mut_data.items():
        for h, u in m.items():
            means[h] += float(u)

    for k in means.keys():
        means[k] = means[k]/len(mutants)

    m_diffs = {}
    for i, m in enumerate(mutants):
        diffs = {}
        for k in WT.keys():
            diffs[k] = float(mut_data[m][k]) - float(mut_data['WT'][k])
        diffs['R:TOTAL + L:TOTAL'] = diffs['Receptor:TOTAL'] + diffs['Ligand:TOTAL']
        m_diffs[m] = diffs
        lst = sorted(diffs.items())
        x, y = zip(*lst)
        ax.bar(index + i * bar_width, y, bar_width, color=colors[i])


    plt.xlim(0, len(diffs.keys()))
    plt.xticks(range(len(diffs.keys())), x, rotation=45)
    ax.legend(mutants)
    ax.grid(True)
    plt.tight_layout()
    plt.title("MMGBSA energetic terms relative to WT")
    plt.show()
