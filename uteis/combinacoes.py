from itertools import combinations
from typing import (
    List,
    Sequence,
    Set,
    Tuple,
    Union,
)


def gera_subconjuntos(conjunto: Union[Set, Sequence],
                      cardinalidade: Union[int, None] = None) -> List[Tuple]:
    """
    Gera todos os subconjuntos do conjunto informado, no formato
    de lista com tuplas constituídas pelos elementos de conjunto.

    Se inteiro cardinalidade for passado, retornará apenas os
    subconjuntos com __len__ == cardinalidade.

    :param cardinalidade:
    :param conjunto:
    :return:
    """
    limite_len_conjunto: int = 20
    if len(conjunto) > limite_len_conjunto:
        raise ValueError('gera_subconjuntos ainda não '
                         'suporta conjuntos maiores que {}'.format(limite_len_conjunto))

    if cardinalidade is not None:
        return [*combinations(conjunto, r=cardinalidade)]

    subconjuntos = []
    for i in range(len(conjunto) + 1):
        subconjuntos.extend([comb
                             for comb
                             in combinations(conjunto,
                                             r=i)])

    return subconjuntos