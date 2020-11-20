import BlackJack
import pygame as pg
import sys
import time

# Настройки скрипта блекджека
dealer = BlackJack.Player('Dealer')
player = BlackJack.Player('igor')
dealer.get_cards(2)
player.get_cards(2)
game_on = False




# настройки PyGame
pg.init()
pg.font.init()
size = width, height = 1280, 960
BLACK = [0, 0, 0]
RED = [255, 0, 0]
GREEN = [0, 80, 0]
BLUE = [0, 0, 255]
WHITE = [255, 255, 255]
GRAY = [180, 180, 180]
screen = pg.display.set_mode(size)
pg.display.update()
pg.display.set_caption('BlackJack')
card_font = pg.font.Font('freesansbold.ttf', 20)

def print_text(result_text):
    text = card_font.render(f"{result_text}", True, RED)
    textRect = text.get_rect(center=(width//2, height//2))
    return screen.blit(text, textRect)

# youlost = card_font.render("YOU LOST", True, RED)
# youlostRect = blackjack.get_rect(center=(width//2, height//2))

def game_over(result):
    screen.fill(GREEN)
    draw_cards(dealer, 50, 100)
    draw_cards(player, 50, 400)
    if result == 'blackjack':
        print_text(result)
    elif result == 'youlost':
        print_text(result)
    elif result == 'youwon':
        print_text(result)

    pg.display.flip()


def suit_color_check(suit):
    if suit == "Hearts" or suit == "Diamonds":
        return RED
    else:
        return BLACK

# cardX,cardY = 50, 50

def draw_cards(name, cardX, cardY):

    for i in range(len(name.cards)):
        cardRect = pg.Rect(cardX+i*90, cardY, 75, 130)
        pg.draw.rect(screen,WHITE,cardRect)
        suit_name = name.cards[i].split()[2]
        if '10' not in name.cards[i]:
            rank_name = name.cards[i].split()[0][0]
        else:
            rank_name = name.cards[i].split()[0][:2]
        suittext = card_font.render(suit_name, True, suit_color_check(suit_name))
        suittextRect = suittext.get_rect(center=(cardX + 35+i*90, cardY + 75))
        ranktext = card_font.render(rank_name, True, suit_color_check(suit_name))
        ranktextRect = suittext.get_rect(center=(cardX+50+i*90, cardY+20))

        screen.blit(suittext, suittextRect)
        screen.blit(ranktext, ranktextRect)


while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    key_press = pg.key.get_pressed()
    if key_press[pg.K_SPACE]:
        player.get_cards(1)
        time.sleep(0.4)
        game_over(None)

    if player.score == 21:
        game_over('blackjack')
        time.sleep(3)
        break
    if player.score > 21:
        game_over('youlost')
        time.sleep(3)
        break
    if key_press[pg.K_LSHIFT]:
        if dealer.score < player.score and dealer.score <= 21:
            dealer.get_cards(1)
            time.sleep(1)
            game_over('None')
        elif dealer.score > player.score and dealer.score <= 21:
            game_over('youlost')
            time.sleep(3)
            break
        elif dealer.score > 21:
            game_over('youwon')
            time.sleep(3)
            break


    game_over(None)


    while game_on:

        while player.score < 21:
            """Player turn"""
            # show_hands()
            turn = input('Выберите "еще" или "хватит"')
            if turn == 'еще':
                player.get_cards(1)
            if turn == 'хватит':
                break

        if player.score > 21:
            """if player got >21 and lost"""
            # show_hands()
            print('Перебор! Вы проиграли')
            break
        elif player.score == 21:
            # show_hands()
            print('BlackJack!')
            break

        if player.score < dealer.score <= 21:
            """проверка перед ходом дилера"""
            # show_hands()
            print('Вы проиграли, у дилера больше')
            break
        else:
            """dealer turn"""
            while dealer.score < player.score:
                dealer.get_cards(1)
                # show_hands()
                print('Дилер взял карту')
            else:
                if player.score < dealer.score <= 21:
                    # show_hands()
                    print('Вы проиграли, у дилера больше')
                    break
                elif dealer.score > 21:
                    # show_hands()
                    print('Перебор у дилера, вы победили')
                    break


