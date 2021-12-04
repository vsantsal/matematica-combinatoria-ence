from itertools import permutations


def lista_02_exercicio_12():
    permutacoes_enunciado = permutations(range(1, 8))
    permutacoes_resultado = []
    for perm in permutacoes_enunciado:
        posicao_1 = perm.index(1) + 1
        posicao_2 = perm.index(2) + 1
        posicao_3 = perm.index(3) + 1
        posicao_4 = perm.index(4) + 1
        posicao_7 = perm.index(7) + 1

        if ((posicao_7 % 2 == 1) and
                abs(posicao_1 - posicao_2) > 1 and
                abs(posicao_3 - posicao_4) == 1):
            permutacoes_resultado.append(perm)

    return permutacoes_resultado


def vae_01_exercicio_05():
    permutacoes_enunciado = permutations([1, 2, 3, 4, 5, 6,
                                          7, 8, 8, 9, 9, 9])
    permutacoes_resultado = []
    for perm in permutacoes_enunciado:
        posicao_1 = perm.index(1)
        posicao_2 = perm.index(2)
        posicao_3 = perm.index(3)

        if posicao_1 < posicao_2 < posicao_3:
            permutacoes_resultado.append(perm)

    return permutacoes_resultado


if __name__ == '__main__':
    resposta_12 = lista_02_exercicio_12()
    print(len(resposta_12))

    reposta_prova = vae_01_exercicio_05()
    print(len(reposta_prova))
