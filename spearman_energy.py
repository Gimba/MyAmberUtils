import sys,argparse
from scipy.stats import spearmanr

def main():
    # parser = argparse.ArgumentParser(description='Calculate spearman rank correlation of two files with energies')
    # parser.add_argument('file1', help='')
    # parser.add_argument('file2', help='')
    #
    # args = parser.parse_args()
    #
    # file_1 = args.file1
    # file_2 = args.file2
    #
    # with open(file_1, 'r') as f1, open(file_2, 'r') as f2:
    #     content1 = f1.readlines()
    #     content2 = f2.readlines()
    #
    #
    #     for l1,l2 in zip(content1,content2):
    # table 1
    # pred = [-94.035, -88.535, -99.015, -97.605, -99.02, -99.685, -93.24, -100.375, -101.16, -99.15, -93.565, -76.835,
    #         -80.585, -86.46,  -92.925, -99.405, -98.29, -102.085, -101.24]
    # exp = [-13.4139702956, -13.1123231598, -15.9803703055, -15.433409785, -15.2925466703, -15.302361193, -15.8584654611, -14.5433371529, -13.9812442761, -15.3862050858, -14.4730140043, -13.407074176, 10, 10, -14.5433371529, -15.0203373936, -15.018002219, -15.2789824272, -15.0663462222]

    # vant Hoff
    pred = [-94.035, -88.535, -99.02, -99.685, -93.24, -101.16, -76.835, -92.925, -99.405, -101.24]
    exp = [154, 230, 3, 9, 30, 68, 100, 30, 6, 1]
    print(spearmanr(pred,exp))


if __name__ == '__main__':
    main()