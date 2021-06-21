import argparse
import os
from datetime import datetime
from typing import Dict, List

import matplotlib.pyplot as plt

from misc.cli_components import DOUBLE_SEPARATOR, SIMPLE_SEPARATOR
from utils.math import compute_distances, join_dict_values
from utils.reader import read_fasta
from utils.sequence import reverse_complement, search_shifted

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path',
                    help="path to FASTA (or Multi-FASTA) file",
                    required=True)
parser.add_argument('--hist',
                    help="generate histogram of size distribution",
                    required=False,
                    action='store_true')


def get_fragments(sequence: str) -> Dict[str, List[int]]:
    """get_fragments computes fragment lengths given a sequence. This function
    reads the sequence with 6 different frames (3 shifts forward and 3 shifts
    in reverse complementary).

    Args:
        sequence (str): DNA or RNA sequence.

    Returns:
        Dict[str, List[int]]: dictionary with all  shifts and its fragments
            lengths stored in lists.
    """
    distances = {}

    sequence_rc = reverse_complement(sequence)

    for shift in [0, 1, 2]:
        positions = search_shifted(sequence, shift)
        distances[f"+{shift+1}F"] = compute_distances(positions)
        positions = search_shifted(sequence_rc, shift)
        distances[f"-{shift+1}R"] = compute_distances(positions)

    return distances


def sizes_histogram(sizes: List[int], seq_name: str):
    bins = 10
    plt.figure(figsize=(8, 6))
    n, bins, patches = plt.hist(sizes, bins=bins, alpha=1, rwidth=0.9)
    plt.xlabel('Size (bp)', size=14)
    plt.ylabel('Count', size=14)
    plt.title(f'Fragment size distribution\n{seq_name}')
    plt.grid(axis='y', alpha=0.75)

    # Create results folder if doesn't exist
    if not os.path.exists('results'):
        os.makedirs('results')

    now = datetime.now()
    timestamp = now.strftime("%m_%d_%Y_%H_%M_%S_%f")
    path = f"results/hist_{timestamp}.png"
    plt.savefig(path)
    print(f"Histogram saved to {path}")


def main():
    args = parser.parse_args()

    sequences = read_fasta(args.path)

    for sequence in sequences:
        print(f"{DOUBLE_SEPARATOR}\n{sequence}\n{DOUBLE_SEPARATOR}")
        print("Shift and direction\tFrag. lengths")
        frags = get_fragments(sequences[sequence])
        for f in frags:
            print(f"{f}\t\t\t{frags[f]}")

        if args.hist:
            print(f"{SIMPLE_SEPARATOR}")
            sizes_histogram(join_dict_values(frags), sequence)
        print(f"{SIMPLE_SEPARATOR}\n")


if __name__ == "__main__":
    main()
