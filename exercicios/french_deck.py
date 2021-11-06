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
