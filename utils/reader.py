from typing import Dict


def read_fasta(path: str) -> Dict[str, str]:
    """read_fasta returns a dictionary with fasta meta and sequences given
       a multi-fasta file.

    Args:
        path (str): path to file.

    Returns:
        Dict[str, str]: dictionary of sequence names and sequences read from
        the file.
    """

    sequences = {}
    current_seq = ''
    is_first = True

    with open(path, 'r') as fasta_file:
        lines = fasta_file.readlines()

    for line in lines:
        if '>' in line and is_first:
            k = line.replace('>', '').strip()
            is_first = False

        elif '>' in line and not is_first:
            sequences[k] = current_seq
            current_seq = ''
            k = line.replace('>', '').strip()

        else:
            current_seq += line.strip()
    sequences[k] = current_seq

    return sequences
