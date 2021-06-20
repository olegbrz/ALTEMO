from utils.reader import read_fasta
from misc.cli_components import SIMPLE_SEPARATOR, DOUBLE_SEPARATOR
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path',
                    help="path to FASTA (or Multi-FASTA) file",
                    required=True)
args = parser.parse_args()

COMPLEMENTS = {"A": "T",
               "C": "G",
               "G": "C",
               "T": "A"}


def reverse(sequence):
    return sequence[::-1]


def reverse_complement(seq):
    return "".join(COMPLEMENTS.get(base, base) for base in reversed(seq))


def main():
    sequences = read_fasta(args.path)

    for sequence in sequences.keys():
        print(f'{DOUBLE_SEPARATOR}\nFASTA: {sequence}\n{DOUBLE_SEPARATOR}')
        print(f"Reverse:\n{reverse(sequences[sequence])}\n")
        print(
            f"Reverse complementary:\n{reverse_complement(sequences[sequence])}")
        print(SIMPLE_SEPARATOR)


if __name__ == "__main__":
    main()
