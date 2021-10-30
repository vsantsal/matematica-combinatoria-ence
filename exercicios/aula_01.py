from itertools import product
import numpy as np
from typing import (
    Dict,
    List,
)


def retorna_produtos_de_dicio_de_bases_e_expoentes(dicio: Dict[int, range]) -> List:
    """
    Função que pode ser útil para resolver exercícios da matéria.

    Passar como input dicionário em que a chave são bases (fatores primos ou não),
    e seus valores são range com expoentes possíveis.
            
    :param dicio:
    :return:
    """
    expoentes = np.array([*product(*dicio.values())])
    bases_produtos = np.array([*dicio.keys()])

    produtos = [np.prod(bases_produtos ** expoente) for expoente in expoentes]
    return produtos


# Exercício 24 da lista
dados_enunciado = {5: range(2),
                   6: range(2),
                   7: range(3),
                   9: range(4)}

produtos_possiveis = retorna_produtos_de_dicio_de_bases_e_expoentes(dados_enunciado)
produtos_possiveis.sort()

print(len(produtos_possiveis))
print(produtos_possiveis)
