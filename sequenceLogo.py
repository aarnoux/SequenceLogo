import sys

ADN = ['A', 'C', 'G', 'T']
ARN = ['U']
PROTEIN = ['I', 'L', 'V', 'F', 'M', 'P', 'S', 'Y', 'W', 'Q', 'N', 'H', 'E', 'D', 'K', 'R']


def count_seq(file):
    count = 0
    for line in file:
        count += 1
        if count == 1:
            alpha = alphabet(line)
    return count, alpha


def alphabet(line):
    if 'U' in line:
        alpha = 'ARN'
    else:
        alpha = 'ADN'
        for char in PROTEIN:
            if char in line:
                alpha = 'PROTEIN'
                break
    return alpha


def main():
    input = sys.argv[1]
    file = open(input, "r")
    seqCount, alpha = count_seq(file)
    print(alpha, seqCount)


if __name__ == '__main__':
    main()