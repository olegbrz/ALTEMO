from typing import Dict, List, Tuple

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
    counts = compute_relative(counts, length, k)

    return counts


def kmers_positions(sequence: str, k: int) -> Dict[str, List[int]]:
    """count_kmers computes the kmers positions given a sequence.

    Args:
        sequence (str): DNA or RNA sequence.
        k (int): k-mer word length.

    Returns: positions absolute and relative counts of kmers.
    """
    positions = {}
    length = len(sequence)

    # K-mer position computing
    for i in range(length-k+1):
        current_kmer = sequence[i:i+k]
        if current_kmer not in positions:
            positions[current_kmer] = [i]
        else:
            positions[current_kmer].append(i)

    return positions


def compute_relative(counts: Dict[str, int], sequence_length: int, k: int) -> Dict[str, Tuple[int, float]]:
    """compute_relative computes the relative occurrence of a kmer given a dict
    of absolute counts and the sequence's length.

    Args:
        counts (Dict[str, int]): kmer counts dictionary.
        sequence_length (int): sequence length (bases).
        k (int): kmer word length.

    Returns:
        Dict[str, Tuple[int, float]]: absolute and relative counts of kmers.
    """
    for count in counts:
        n = counts[count]
        counts[count] = (n, round(n/(sequence_length-k+1), 6))
    return counts
