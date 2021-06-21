from utils.reader import read_fasta
from utils.kmer import count_kmers, g_counts
from misc.cli_components import SIMPLE_SEPARATOR, DOUBLE_SEPARATOR
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path',
                    help="path to FASTA (or Multi-FASTA) file",
                    required=True)
parser.add_argument('-k',
                    help="k-mer word length",
                    type=int,
                    required=True)


def main():
    args = parser.parse_args()
    sequences = read_fasta(args.path)
    results = {k: count_kmers(sequences[k], args.k) for k in sequences.keys()}
    global g_counts

    # Local counts
    for sequence in results:
        print(f"{DOUBLE_SEPARATOR}\n{sequence}\n{DOUBLE_SEPARATOR}")
        print("k-mer\tCount\tRelative")
        for kmer in results[sequence]:
            print(
                f"{kmer}\t{results[sequence][kmer][0]}\t{results[sequence][kmer][1]}")
        print(f"{SIMPLE_SEPARATOR}\n")

    # Global counts
    print(f"{DOUBLE_SEPARATOR}\nGLOBAL COUNTS\n{DOUBLE_SEPARATOR}")
    print("k-mer\tCount")
    for kmer in g_counts:
        print(
            f"{kmer}\t{g_counts[kmer]}")
    print(f"{SIMPLE_SEPARATOR}")


if __name__ == "__main__":
    main()
