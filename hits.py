import argparse

from misc.cli_components import SIMPLE_SEPARATOR, DOUBLE_SEPARATOR
from utils.reader import read_fasta
from utils.kmer import kmers_positions

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path',
                    nargs='+',
                    help="path to FASTA file (required to provide exactly 2 files)",
                    required=True)
parser.add_argument('-k',
                    help="k-mer word length",
                    type=int,
                    required=True)


def main():
    args = parser.parse_args()

    # Check if 2 files were provided
    if len(args.path) != 2:
        raise ValueError("Please provide exactly 2 fasta files in arguments.")

    sequence1 = read_fasta(args.path[0])
    kmers_positions1 = kmers_positions(list(sequence1.values())[0], args.k)

    sequence2 = read_fasta(args.path[1])
    kmers_positions2 = kmers_positions(list(sequence2.values())[1], args.k)

    print(
        f'{DOUBLE_SEPARATOR}\n{list(sequence1.keys())[0]}\n{DOUBLE_SEPARATOR}')
    for kmer in kmers_positions1:
        print(f'{kmer}: {kmers_positions1[kmer]}')
    print(SIMPLE_SEPARATOR)

    print(
        f'{DOUBLE_SEPARATOR}\n{list(sequence2.keys())[0]}\n{DOUBLE_SEPARATOR}')
    for kmer in kmers_positions2:
        print(f'{kmer}: {kmers_positions2[kmer]}')
    print(SIMPLE_SEPARATOR)


if __name__ == "__main__":
    main()
