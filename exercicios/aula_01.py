from itertools import product
import numpy as np


# Exercício 24 da lista
dados_enunciado = {5: range(2),
                   6: range(2),
                   7: range(3),
                   9: range(4)}

expoentes = np.array([*product(*dados_enunciado.values())])
bases_produtos = np.array([*dados_enunciado.keys()])

produtos_possiveis = [np.prod(bases_produtos**expoente) for expoente in expoentes]
produtos_possiveis.sort()

print(len(produtos_possiveis))
print(produtos_possiveis)
