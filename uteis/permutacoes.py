from itertools import permutations
from math import comb, factorial
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


def numero_de_permutacoes_caoticas(n: int) -> int:
    n_fat: int = factorial(n)
    fator: int = sum(((-1)**i)/factorial(i) for i in range(n+1))
    return int(n_fat*fator)


def numero_de_permutacoes_caoticas_com_elementos_fixos(n_elementos: int, n_fixos: int) -> int:
    c_n_m: int = comb(n_elementos, n_fixos)
    perms_caoticas_elementos_restantes: int = numero_de_permutacoes_caoticas(n_elementos-n_fixos)
    return c_n_m * perms_caoticas_elementos_restantes
