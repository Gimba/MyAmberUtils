#! /usr/bin/env python


def main():
    with open("FINAL_DECOMP_MMPBSA.csv", 'r') as f:
        lines = f.readlines()
        totals_column = lines[7].split(',').index('TOTAL')

        decomp_total = 0.0

        for line in lines[9:]:
            line = line.split(',')
            if len(line) >= 17:
                decomp_total += float(line[totals_column])

        print("Decomp total:", round(decomp_total,2))

    with open("../mmpbsa/bounds/sum.txt", 'r') as g:
        last_line = g.readlines()[-1]
        mmgbsa_total = float(last_line.split()[2])

    print("MMGBSA total:",mmgbsa_total)

    diff = decomp_total-mmgbsa_total
    print("Difference:", round(diff,2))

if __name__ == '__main__':
    main()