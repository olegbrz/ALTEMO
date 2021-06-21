from utils.reader import read_fasta
from utils.sequence import reverse, reverse_complement
from misc.cli_components import SIMPLE_SEPARATOR, DOUBLE_SEPARATOR
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path',
                    help="path to FASTA (or Multi-FASTA) file",
                    required=True)


def main():
    args = parser.parse_args()
    sequences = read_fasta(args.path)

    for sequence in sequences.keys():
        print(f'{DOUBLE_SEPARATOR}\nFASTA: {sequence}\n{DOUBLE_SEPARATOR}')
        print(f"Reverse:\n{reverse(sequences[sequence])}\n")
        print(
            f"Reverse complementary:\n{reverse_complement(sequences[sequence])}")
        print(SIMPLE_SEPARATOR)


if __name__ == "__main__":
    main()
