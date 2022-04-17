import BlackJack
import pygame as pg
import sys
import time
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Настройки скрипта блекджека
dealer = BlackJack.Player('Dealer')
player = BlackJack.Player('igor')
# dealer.get_cards(2)
# player.get_cards(2)
welcome = True
game_on = True
player_turn = True
dealer_turn = True
replay = True

# настройки PyGame
pg.init()
pg.font.init()
size = width, height = 800, 600
BLACK = [0, 0, 0]
RED = [255, 0, 0]
GREEN = [0, 80, 0]
BLUE = [0, 0, 255]
WHITE = [255, 255, 255]
GRAY = [180, 180, 180]
GRAY2 = [120, 120, 120]
GRAY3 = [240, 220, 220]
screen = pg.display.set_mode(size)
pg.display.update()
pg.display.set_caption('BlackJack')
card_font = pg.font.Font('freesansbold.ttf', 25)
result_font = pg.font.Font('freesansbold.ttf', 30)


def print_text(result_text, textX, textY, color, backgrond=None):
    """Печатает заданный в 1 аргументе текст"""
    text = result_font.render(f"{result_text}", True, color, backgrond)
    textRect = text.get_rect(center=(textX, textY))
    return screen.blit(text, textRect)


def screen_draw():
    screen.fill(GREEN)
    draw_cards(dealer, 100, 100)
    draw_cards(player, 100, 280)
    draw_buttons(200, 500, 'STAY', 'HIT')
    if len(dealer.cards) == 1:
        hidden_card = pg.image.load(resource_path("back.png"))
        hidden_cardRect = hidden_card.get_rect(center=(100 + 115 + 45, 100 + 65))
        screen.blit(hidden_card, hidden_cardRect)


def suit_color_check(suit):
    """возвращает РЕД или БЛЕК для функции draw_cards()"""
    if suit == "Hearts" or suit == "Diamonds":
        return RED
    else:
        return BLACK


# cardX,cardY = 50, 50
def draw_buttons(buttonX, buttonY, but_text1, but_text2):
    for i in range(2):
        moreRectborder = pg.Rect(buttonX + i * 150, buttonY, 130, 75)
        moreRectmain = pg.Rect(buttonX + 5 + i * 150, buttonY + 5, 120, 65)
        pg.draw.rect(screen, GRAY2, moreRectborder)
        pg.draw.rect(screen, GRAY, moreRectmain)
        if i == 1:
            print_text(f'{but_text1}', buttonX + 65 + i * 150, buttonY + 40, BLACK)
        else:
            print_text(f'{but_text2}', buttonX + 65, buttonY + 40, BLACK)


def draw_cards(name, cardX, cardY):
    """Отрисовывает на экран карты игрока 'name'"""

    for i in range(len(name.cards)):
        cardRect = pg.Rect(cardX + i * 115 + 5, cardY + 5, 80, 120)
        cardborderRect = pg.Rect(cardX + i * 115, cardY, 90, 130)
        pg.draw.rect(screen, WHITE, cardborderRect)
        pg.draw.rect(screen, BLACK, cardRect, 1)

        suit_name = name.cards[i].split()[2]
        suit_pic = pg.image.load(resource_path(f"{suit_name}.png"))
        suit_picRect = suit_pic.get_rect(center=(cardX + 47 + i * 115, cardY + 75))
        if '10' not in name.cards[i]:
            rank_name = name.cards[i].split()[0][0]
        else:
            rank_name = name.cards[i].split()[0][:2]
        ranktext = card_font.render(rank_name, True, suit_color_check(suit_name))
        ranktextRect = ranktext.get_rect(center=(cardX + 20 + i * 115, cardY + 22))

        screen.blit(suit_pic, suit_picRect)
        screen.blit(ranktext, ranktextRect)
    if name == dealer:
        print_text('Карты дилера', cardX + 120, cardY - 35, BLACK, GRAY)
    elif name == player:
        print_text('Ваши карты', cardX + 120, cardY + 165, BLACK, GRAY)


while game_on:

    while welcome:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.MOUSEBUTTONUP:
                if width // 2 - 150 <= pg.mouse.get_pos()[0] <= width // 2 - 15 and \
                        height // 2 + 100 <= pg.mouse.get_pos()[1] <= height // 2 + 175:
                    welcome = False

        screen.fill(GRAY3)
        print_text('Добро пожаловать в игру Black Jack', width // 2, height // 2 - 200, BLACK)
        print_text('Управление: "HIT" - взять еще одну карту', width // 2, height // 2 - 160, BLACK)
        print_text('"STAY" - достаточно, передать ход дилеру', width // 2, height // 2 - 120, BLACK)
        print_text('Для начала игры нажми "HIT"', width // 2, height // 2 - 80, BLACK)
        draw_buttons(width // 2 - 150, height // 2 + 100, 'STAY', 'HIT')
        pg.display.flip()

    while player_turn:

        if len(player.cards) == 0:
            player.get_cards(2)
            dealer.get_cards(1)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            if event.type == pg.MOUSEBUTTONUP:
                if 200 <= pg.mouse.get_pos()[0] <= 330 and 500 <= pg.mouse.get_pos()[1] <= 575:
                    player.get_cards(1)
                if 350 <= pg.mouse.get_pos()[0] <= 480 and 500 <= pg.mouse.get_pos()[1] <= 575:
                    player_turn = False
                    print_text('Хватит. Ход дилера..', width // 2, height // 2 - 45, RED)
                    pg.display.flip()
                    time.sleep(1)

        if player.score > 21:
            replay = True
            dealer_turn = False
            screen_draw()
            print_text('Перебор! Вы проиграли!', width // 2, height // 2 - 45, RED)
            pg.display.flip()
            time.sleep(3)
            player_turn = False
        if player.score == 21:
            replay = True
            dealer_turn = False
            screen_draw()
            print_text('Black Jack! Вы победили!', width // 2, height // 2 - 45, RED)
            pg.display.flip()
            time.sleep(3)
            player_turn = False

        screen_draw()

        pg.display.flip()

    while dealer_turn:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        if dealer.score <= 21 and dealer.score <= player.score:
            dealer.get_cards(1)
            screen_draw()
            pg.display.flip()
            time.sleep(2)

        if dealer.score <= 21 and dealer.score > player.score:
            replay = True
            player_turn = False
            screen_draw()
            print_text('У дилера больше! Вы проиграли!', width // 2, height // 2 - 45, RED)
            pg.display.flip()
            time.sleep(3)
            dealer_turn = False

        if dealer.score > 21:
            replay = True
            player_turn = False
            screen_draw()
            print_text('Перебор у дилера! Вы победили!', width // 2, height // 2 - 45, RED)
            pg.display.flip()
            time.sleep(3)
            dealer_turn = False

    while replay:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.MOUSEBUTTONUP:
                if width // 2 - 150 <= pg.mouse.get_pos()[0] <= width // 2 - 15 and \
                        height // 2 + 40 <= pg.mouse.get_pos()[1] <= height // 2 + 115:
                    player_turn = True
                    dealer_turn = True
                    player.clear_hand()
                    dealer.clear_hand()
                    BlackJack.deck_generator()
                    replay = False

                # if event.type == pg.KEYDOWN:
                #     if event.key == pg.K_LSHIFT:
                if width // 2 <= pg.mouse.get_pos()[0] <= width // 2 + 135 and \
                        height // 2 + 40 <= pg.mouse.get_pos()[1] <= height // 2 + 115:
                    sys.exit()

        screen.fill(GREEN)
        print_text('Хотите сыграть еще?', width // 2, height // 2, RED)
        draw_buttons(width // 2 - 150, height // 2 + 40, 'No', 'Yes')
        pg.display.flip()
