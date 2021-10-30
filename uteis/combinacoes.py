from itertools import combinations
from typing import (
    List,
    Set,
    Tuple,
)


def gera_subconjuntos(conjunto: Set) -> List[Tuple]:
    """
    Gera todos os subconjuntos do conjunto informado, no formato
    de lista com tuplas constituídas pelos elementos de conjunto.

    :param conjunto:
    :return:
    """
    subconjuntos = []
    for i in range(len(conjunto) + 1):
        subconjuntos.extend([comb
                             for comb
                             in combinations(conjunto,
                                             r=i)])

    return subconjuntos
