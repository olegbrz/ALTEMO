from typing import Dict, List
from functools import reduce


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


def join_dict_values(dictionary: Dict):
    return reduce(lambda x, y: x+y, list(dictionary.values()))
