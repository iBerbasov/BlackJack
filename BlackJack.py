import random

deck = []


def deck_generator():
    """Generates deck of 52 cards"""
    deck.clear()
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank} of {suit}')

    random.shuffle(deck)


def pick_card():
    """берет из колоды карту"""
    return deck.pop()


class Player:
    """ карты игрока """

    def __init__(self, name):
        self.name = name
        self.cards = []
        self.__score = 0

        if not deck:
            deck_generator()

    def get_cards(self, card_amount):
        """ берет заданое кол-во карт из списка deck, вставляет в список self.cards"""
        for i in range(card_amount):
            self.cards.append(pick_card())
        self.score_count()

    def clear_hand(self):
        """ удаляет все карты игрока"""
        self.cards.clear()
        self.score_count()

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, amount):
        self.__score = amount

    def score_count(self):
        if self.cards:
            self.__score = 0
            for card in self.cards:
                if "Jack" in card or "Queen" in card or "King" in card:
                    self.__score += 10
                elif "Ace" in card:
                    self.__score += 11
                else:
                    self.__score += int(card.split()[0])
            if self.__score > 21:
                for card in self.cards:
                    if "Ace" in card:
                        self.__score -= 10
                        if self.__score <= 21:
                            break

    # def ace_check(self):
    #     aces = 0
    #     for card in self.cards:
    #         if "Ace" in card:
    #             aces += 1
    #     return aces

    # def game_result_check(self):
    #     """проверяет сумму очков игрока:
    #         пока сумма меньше 21 - возвращает True
    #         если 21 - False
    #         если перебор - проверяет наличие тузов в руке и снижает сумму на 10 за каждого туза
    #         если тузов нет или перебор остается - возвращает False - проигрыш
    #         """
    #
    #     if self.score == 21:
    #         # print('BlackJack!')
    #         return 21
    #     elif self.score < 21:
    #         return self.__score
    #     elif self.score > 21:
    #         # if self.ace_check():
    #         #     self.__score -= 10 * self.ace_check()
    #         #     return self.__score
    #         if:
    #             return self.__score
