from typing import Dict, Tuple
from utils.reader import read_fasta
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
args = parser.parse_args()

g_counts = {}


def count_kmers(sequence: str, k: int) -> Dict[str, Tuple[int, float]]:
    """count_kmers counts absolute and relative kmer occurence given a sequence.

    Args:
        sequence (str): DNA or RNA sequence.
        k (int): k-mer word length.

    Returns:
        Dict[str, Tuple[int, float]]: absolute and relative counts of kmers.
    """
    global g_count
    counts = {}
    length = len(sequence)

    # K-mer counting
    for i in range(length-k+1):
        current_kmer = sequence[i:i+k]
        # Local counting
        if current_kmer not in counts:
            counts[current_kmer] = 1
        else:
            counts[current_kmer] += 1
        # Global counting
        if current_kmer not in g_counts:
            g_counts[current_kmer] = 1
        else:
            g_counts[current_kmer] += 1

    # Relative count computing
    counts = compute_relative(counts, length)

    return counts


def compute_relative(counts: Dict[str, int], sequence_length: int) -> Dict[str, Tuple[int, float]]:
    """compute_relative computes the relative occurrence of a kmer given a dict
    of absolute counts and the sequence's length.

    Args:
        counts (Dict[str, int]): kmer counts dictionary.
        sequence_length (int): sequence length (bases).

    Returns:
        Dict[str, Tuple[int, float]]: absolute and relative counts of kmers.
    """
    for count in counts:
        n = counts[count]
        counts[count] = (n, round(n/sequence_length, 6))
    return counts


def main():
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


if __name__ == '__main__':
    main()
