import unittest
import BlackJack


class TestCap(unittest.TestCase):

    # def test_1card_pick(self):
    #
    #     igor = BlackJack.Player("Igor")
    #     igor.get_cards(2)
    #     result = len(igor.cards)
    #     self.assertEqual(result, 2)
    #
    # def test_2secondplayer_card_pick(self):
    #
    #     dealer = BlackJack.Player("Igor")
    #     dealer.get_cards(2)
    #     result = len(dealer.cards)
    #     self.assertEqual(result, 2)

    # def test_3score_count(self):
    #     igor = BlackJack.Player("Igor")
    #     igor.get_cards(3)
    #
    #     print('test3.1', len(BlackJack.deck))
    #     print('test3.2', igor.cards)
    #     # print(igor.score, 'test3.3')
    #
    #     igor.get_cards(1)
    #     print('test3.4', igor.cards)
    #     # print(igor.score, 'test3.5')
    #
    # def test_4ace_check(self):
    #     igor = BlackJack.Player("Igor")
    #     igor.get_cards(10)
    #     print('test4.1', igor.cards)
    #     result = igor.ace_check()
    #     print('test4.2', result)

    def test_5dealer_ace_check(self):
        player = BlackJack.Player('igor')
        player.cards.append('Ace')
        player.score_count()
        print(player.score, player.cards)

        player.cards.append('Ace')
        player.score_count()
        print(player.score, player.cards)

        player.cards.append('8 of diamond')
        player.score_count()
        print(player.score, player.cards)

        player.cards.append('Ace')
        player.score_count()
        print(player.score, player.cards)

        player.cards.append('2 of diamond')
        player.score_count()
        print(player.score, player.cards)


if __name__ == '__main__':
    unittest.main()
