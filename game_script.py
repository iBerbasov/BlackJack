import BlackJack

dealer = BlackJack.Player('Dealer')
player = BlackJack.Player('igor')


def show_hands():
    print('\n' * 2)
    print([dealer.cards], ' - Карты дилера', dealer.score)
    print(player.cards, ' - Ваши карты', player.score)


dealer.get_cards(2)
player.get_cards(2)

# game_on = True

while True:

    while player.score < 21:
        """Player turn"""
        show_hands()
        turn = input('Выберите "еще" или "хватит"')
        if turn == 'еще':
            player.get_cards(1)
        if turn == 'хватит':
            break

    if player.score > 21:
        """if player got >21 and lost"""
        show_hands()
        print('Перебор! Вы проиграли')
        break
    elif player.score == 21:
        show_hands()
        print('BlackJack!')
        break

    if player.score < dealer.score <= 21:
        """проверка перед ходом дилера"""
        show_hands()
        print('Вы проиграли, у дилера больше')
        break
    else:
        """dealer turn"""
        while dealer.score < player.score:
            dealer.get_cards(1)
            show_hands()
            print('Дилер взял карту')
        else:
            if player.score < dealer.score <= 21:
                show_hands()
                print('Вы проиграли, у дилера больше')
                break
            elif dealer.score > 21:
                show_hands()
                print('Перебор у дилера, вы победили')
                break
