COMPLEMENTS = {"A": "T",
               "C": "G",
               "G": "C",
               "T": "A"}


def reverse(sequence):
    return sequence[::-1]


def reverse_complement(seq):
    return "".join(COMPLEMENTS.get(base, base) for base in reversed(seq))
