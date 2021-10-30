from itertools import combinations
from typing import (
    List,
    Set,
    Tuple,
)


def gera_subconjuntos(conjunto: Set) -> List[Tuple]:
    """
    Gera subconjuntos do conjunto informado.

    :param conjunto:
    :return:
    """
    limite_len_conjunto: int = 20
    if len(conjunto) > limite_len_conjunto:
        raise ValueError('gera_subconjuntos ainda não '
                         'suporta conjuntos maiores que {}'.format(limite_len_conjunto))

    subconjuntos = []
    for i in range(len(conjunto) + 1):
        subconjuntos.extend([comb
                             for comb
                             in combinations(conjunto,
                                             r=i)])

    return subconjuntos
