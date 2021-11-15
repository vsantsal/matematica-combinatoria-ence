import operator
from collections import namedtuple
from itertools import combinations
from typing import Iterable


Restricao = namedtuple('Restricao', 'operador valor')


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        if other.rank is None:
            return self.suit == other.suit

        if other.suit is None:
            return self.rank == other.rank

        return self.rank == other.rank and self.suit == other.suit

    def __str__(self):
        return 'Rank: {} Suit: {}'.format(self.rank, self.suit)


class FrenchDeck:
    """
    Implementação de Luciano Ramalho em Python Fluente.
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    @property
    def cards(self):
        return self._cards

    def ordena_deck(self):
        def spades_high(card):
            suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
            rank_value = self.ranks.index(card.rank)
            return rank_value * len(suit_values) + suit_values[card.suit]

        self._cards = sorted(self._cards, key=spades_high)


def numero_combinacoes_com_restricao_para_soma_elementos(iteravel: Iterable,
                                                         escolhas: int,
                                                         restricao: Restricao) -> int:
    """
    Função para retornar número de combinações de um iteravel para escolhas cuja
    soma atende à restricao informada.

    >>>numero_combinacoes_com_restricao_para_soma_elementos(range(4), 3, Restricao(operator.ge, 2))
    4

    :param iteravel:
    :param escolhas:
    :param restricao:
    :return:
    """
    combins = combinations(iteravel, escolhas)
    combins_da_restricao = [comb for comb in combins
                            if restricao.operador(sum(comb), restricao.valor)]
    return len(combins_da_restricao)


def numero_combinacoes_com_restricao_para_identidade_elementos(iteravel: Iterable,
                                                               escolhas: int,
                                                               valor_alvo,
                                                               quantidade: int) -> int:
    combins = combinations(iteravel, escolhas)
    contador = 0
    for comb in combins:
        elementos = [el for el in comb if el == valor_alvo]
        if len(elementos) == quantidade:
            contador += 1
    return contador


if __name__ == '__main__':
    # exercício 13
    restricao_enunciado = Restricao(operador=operator.ge, valor=9)
    numeros_urna = range(1, 11)
    numero_escolhas = 3
    num_combinacoes = numero_combinacoes_com_restricao_para_soma_elementos(numeros_urna,
                                                                           numero_escolhas,
                                                                           restricao_enunciado)
    print(num_combinacoes)  # 116 combinações

    # Exercício 14
    valor_procurado = Card(rank='A', suit=None)
    baralho = FrenchDeck()
    numero_escolhas = 5
    vezes_valor_procurado = 3
    num_combinacoes = numero_combinacoes_com_restricao_para_identidade_elementos(baralho,
                                                                                 numero_escolhas,
                                                                                 valor_procurado,
                                                                                 vezes_valor_procurado)

    print(num_combinacoes)  # 4512 combinações
