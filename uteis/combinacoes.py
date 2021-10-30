from itertools import (
    combinations,
    chain
)
from typing import (
    Iterator,
    List,
    Sequence,
    Set,
    Tuple,
    Union,
)


def gera_subconjuntos(conjunto: Union[Set, Sequence],
                      cardinalidade: Union[int, None] = None,
                      gerador: bool = False) -> Union[List[Tuple], Iterator[Tuple]]:
    """
    Gera todos os subconjuntos do conjunto informado, no formato
    de lista com tuplas constituídas pelos elementos de conjunto.

    Se inteiro cardinalidade for passado, retornará apenas os
    subconjuntos com __len__ == cardinalidade.

    :param gerador:
    :param cardinalidade:
    :param conjunto:
    :return:
    """
    # se cardinalidade for None, retornaremos combinações de 0 a 0 até n a n dos elementos do conjunto
    # caso contrário, apenas as combinações de cardinalidade a cardinalidade
    iterador = (chain.from_iterable(combinations(conjunto, i) for i in range(len(conjunto) + 1))
                if cardinalidade is None else combinations(conjunto, r=cardinalidade))

    # condicional para impedir que usuários tentem
    # retornar lista para conjuntos grandes
    # (dada a complexidade de tempo da função, números a partir de 20
    # podem consumir memória e tempo excessivos)
    if not gerador:
        limite_len_conjunto: int = 20
        if len(conjunto) > limite_len_conjunto:
            raise ValueError('gera_subconjuntos ainda não '
                             'suporta conjuntos maiores que {}'.format(limite_len_conjunto))
        iterador = [*iterador]

    return iterador
