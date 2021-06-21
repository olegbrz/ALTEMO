from typing import List


COMPLEMENTS = {"A": "T",
               "C": "G",
               "G": "C",
               "T": "A"}

STOP_CODONS = ["TAA", "TAG", "TGA"]


def reverse(sequence):
    return sequence[::-1]


def reverse_complement(seq):
    return "".join(COMPLEMENTS.get(base, base) for base in reversed(seq))


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
