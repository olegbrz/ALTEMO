from misc.cli_components import DOUBLE_SEPARATOR, SIMPLE_SEPARATOR
from typing import List, Dict
from utils.reader import read_fasta
from sequence_util import reverse_complement
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path',
                    help="path to FASTA (or Multi-FASTA) file",
                    required=True)

STOP_CODONS = ["TAA", "TAG", "TGA"]


def search_shifted(sequence: str, shift=0, search: List[str] = STOP_CODONS) -> List[int]:
    """search_shifted searrches all position of given list of codons on a sequence.
    The function supports read frame shifting.


    Args:
        sequence (str): DNA or RNA sequence.
        shift (int, optional): Reading frame shift. Defaults to 0.
        search (List[str], optional): List of codons to search. Defaults to STOP_CODONS.

    Returns:
        List[int]: list of positions of given codons.
    """
    shift = shift % 3
    positions = [shift]
    for i in range(shift, len(sequence)-3+1, 3):
        codon = sequence[i:i+3]
        if codon in search:
            positions.append(i+3)
    positions.append(len(sequence))
    return positions


def compute_distances(positions: List[int]) -> List[int]:
    """compute_distances this function computes the distance between all consequent
    numbers in a list. E.g:

    Input: [1, 5, 11]
    Output: [4, 6]


    Args:
        positions (List[int]): list of positions (integers).

    Returns:
        List[int]: list of distances (integers).
    """
    return [positions[i+1]-positions[i] for i in range(len(positions)-1)]


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

    for shift in [0, 1, 2]:
        positions = search_shifted(sequence_rc, shift)
        distances[f"-{shift+1}R"] = compute_distances(positions)

    return distances


def main():
    args = parser.parse_args()

    sequences = read_fasta(args.path)

    for sequence in sequences:
        print(f"{DOUBLE_SEPARATOR}\n{sequence}\n{DOUBLE_SEPARATOR}")
        print("Shift and direction\tFrag. lengths")
        frags = get_fragments(sequences[sequence])
        for f in frags:
            print(f"{f}\t\t\t{frags[f]}")
        print(f"{SIMPLE_SEPARATOR}\n")


if __name__ == "__main__":
    main()
