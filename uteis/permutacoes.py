from itertools import permutations
from typing import List, Tuple


def _get_int_from_positional_tuple(tupla: Tuple[int], base: int = 10) -> int:
    resultado: int = 0
    for posicao, valor in enumerate(tupla):
        resultado += valor*(base**posicao)
    return resultado


def posicao_de_numero_em_permutacoes_algarismos(numero: int,
                                                ordem_decrescente: bool = False) -> int:

    algarismos: List[int] = [int(alg) for alg in str(numero)]
    permutacoes_algarismos: List[int] = [_get_int_from_positional_tuple(perm)
                                         for perm
                                         in permutations(algarismos)]
    permutacoes_algarismos.sort(reverse=ordem_decrescente)
    return permutacoes_algarismos.index(numero) + 1
