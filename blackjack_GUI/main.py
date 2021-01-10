'''
Author Name     : Badrikesh Prusty
Date            : 20/12/2020
Description     : To develop Blackjack game (GUI version) using python's pygame library
'''


from image_load_transform import *
from random import shuffle
import time

# initialize pygame
pygame.init()

# Color
forest_green = (34,  139, 34)            # RGB values of forest green color
white        = (255, 255, 255)


# Game window configuration
size = width, height = (800, 600)       # window size
fps                  = 60               # game frame rate
seconds              = time.time()      # assigning current epoch time value



# All Fonts and texts

# Fonts. Loading fonts from the current directory
#                           Font Name          size
font1 = pygame.font.Font('fonts/roboto-bold.ttf',     28)  # Bold
font2 = pygame.font.Font('fonts/roboto-regular.ttf',  18)  # Regular
font3 = pygame.font.Font('fonts/roboto-light.ttf',    20)  # Light
font4 = pygame.font.Font('fonts/roboto-regular.ttf',  20)  # Regular
font5 = pygame.font.Font('fonts/roboto-regular.ttf',  16)  # Regular
font6 = pygame.font.Font('fonts/roboto-regular.ttf',  28)  # Regular

# Loading screen texts
load_txt      = font1.render("Loading...",                True, white)
continue_txt  = font1.render("Press any key to continue", True, white)

place_bet_txt = font6.render("Place Your Bet",            True, white)

# Game Result text
win_txt  = font1.render("You Win!!",    True, white)
lose_txt = font1.render("You Lose!!",   True, white)
draw_txt = font1.render("Match Draw!!", True, white)

# Game Over text
over_continue_txt = font4.render("Press any key to continue", True, white)

# If bet exceeds total amount
invalid_bet_txt   = font4.render("Entered Bet not valid",     True, white)
tamt_less_txt     = font4.render("Total Amount Insufficient", True, white)

# Icon Texts
restart_txt = font2.render("Restart", True, white)
stand_txt   = font5.render("Stand",   True, white)
hit_txt     = font5.render("Hit",     True, white)
double_txt  = font5.render("Double",  True, white)

# Player info text
dealer_txt  = font4.render("Dealer",  True, white)
bet_txt     = font4.render('Bet($)',  True, white)
count_txt   = font4.render('Count',   True, white)

# Text to indicate to enter name and amount for player
enter_name   = font2.render("Enter Name ",       True, white)
enter_amount = font2.render("Total Amount ($) ", True, white)


# list to store the count as per the individual cards
dealer_count = []
player_count = []



# Default values
default_name   = 'Player'
default_amount = '1000'
default_bet    = '10'

# Setting everything as default value initially
player_name   = default_name
total_amount  = default_amount
curr_bet      = default_bet
temp_bet      = default_bet



# Creating rectangle for text box for user input 
pname_box     = pygame.Rect(300, 345, 200, 30)
total_amt_box = pygame.Rect(300, 390, 200, 30)

# Creating boxex for all the gameplay icons add mouse-click support on icons
restart_box     = pygame.Rect(6,   520, 62, 70)
stand_box       = pygame.Rect(291, 475, 40, 70)
hit_box         = pygame.Rect(447, 475, 48, 70)
double_box      = pygame.Rect(367, 475, 46, 70)

curr_amt_box    = pygame.Rect(340, 565, 100, 27)
place_bet_box   = pygame.Rect(343, 390, 100, 30)

# Clickable continue buttons
playicon_box    = pygame.Rect(360, 450, 64, 64)
betplayicon_box = pygame.Rect(360, 435, 64, 64)


# Colors for text boxes
# Colors for text box to indicate that it is active for typing
active_color  = pygame.Color("green")        # active
passive_color = pygame.Color("darkgrey")     # inactive

# Setting default color of text boxes
pnamebox_color  = passive_color
amtbox_color    = passive_color
betbox_color    = passive_color


# Flags
loading_flag    = True
run_once_flg    = True
restart_flg     = False
insuff_amt_flg  = False
double_flg      = False


# For reading and assigning keyboard inputs
pnamebox_active      = False     # Disable text inputs for player name
amtbox_active        = False     # Disable amountbox text inputs
betbox_active        = False     # Disable key input for bet

# For reading mouse events and display items
inp_name_amt_active  = False     # Activate text boxes for keyboard input for name and amount
inp_bet_active       = False     # Activate text box to input bet


# For keyboard, mouse or display events active
config_player_active    = False

# mouse click events
playicon_box_active     = False
betplayicon_box_active  = False
game_buttons_active     = False
restart_button_active   = False

game_ready_active_disp  = False

game_over_key_active    = False


# Setting clock for setting frame rate of the game
clock = pygame.time.Clock()

# setting screen size
screen = pygame.display.set_mode(size)

# setting title bar icon and title
pygame.display.set_caption("BlackJack")
pygame.display.set_icon(icon)


# Icon initial position
icon_x, icon_y = 336, 380       # initial_icon coordinates

i = 1                           # index card_deck initial value


# To store the total count
player_tcount = 0
dealer_tcount = 0


# List containing all the cards in the order
card_deck = [spade_A,   spade_2,   spade_3,   spade_4,   spade_5,   spade_6,     spade_7,    spade_8,
             spade_9,   spade_10,  spade_J,   spade_Q,   spade_K,   diamond_A,   diamond_2,  diamond_3,
             diamond_4, diamond_5, diamond_6, diamond_7, diamond_8, diamond_9,   diamond_10, diamond_J, 
             diamond_Q, diamond_K, heart_A,   heart_2,   heart_3,   heart_4,     heart_5,    heart_6,   
             heart_7,   heart_8,   heart_9,   heart_10,  heart_J,   heart_Q,     heart_K,    club_A,
             club_2,    club_3,    club_4,    club_5,    club_6,    club_7,      club_8,     club_9,
             club_10,   club_J,    club_Q,    club_K]

card_A    = [spade_A,  diamond_A,  heart_A,  club_A]
card_2    = [spade_2,  diamond_2,  heart_2,  club_2]
card_3    = [spade_3,  diamond_3,  heart_3,  club_3]
card_4    = [spade_4,  diamond_4,  heart_4,  club_4]
card_5    = [spade_5,  diamond_5,  heart_5,  club_5]
card_6    = [spade_6,  diamond_6,  heart_6,  club_6]
card_7    = [spade_7,  diamond_7,  heart_7,  club_7]
card_8    = [spade_8,  diamond_8,  heart_8,  club_8]
card_9    = [spade_9,  diamond_9,  heart_9,  club_9]
card_10   = [spade_10, diamond_10, heart_10, club_10, 
             spade_J,  diamond_J,  heart_J,  club_J,
             spade_Q,  diamond_Q,  heart_Q,  club_Q, 
             spade_K,  diamond_K,  heart_K,  club_K]


dealer_back_card = [red_back,  purple_back, yellow_back,
                    gray_back, blue_back,   green_back]


# List to store the cards for each player
player_card = []
dealer_card = []


# Function to compare the card value and return the count 
def card_value(curr_card):
    if curr_card in card_A:
        return 11

    elif curr_card in card_2:
        return 2

    elif curr_card in card_3:
        return 3

    elif curr_card in card_4:
        return 4

    elif curr_card in card_5:
        return 5
    
    elif curr_card in card_6:
        return 6

    elif curr_card in card_7:
        return 7

    elif curr_card in card_8:
        return 8

    elif curr_card in card_9:
        return 9

    elif curr_card in card_10:
        return 10


# Function to place the game icon in specified coordinates
def place_icon(x, y):
    screen.blit(icon, (x, y))


# Function to load the texts at the start of the game
def disp_loading_txt():
    screen.blit(load_txt, (338, 505))


def disp_continue_txt():
    screen.blit(continue_txt, (248, 505))


def clk_enable_inp_name():
    global pnamebox_active, pnamebox_color, amtbox_active, amtbox_color
    global player_name, total_amount

    pnamebox_active = True          # activate text box input
    pnamebox_color = active_color   # change the color to active
    amtbox_active = False           # disable other text box
    amtbox_color = passive_color

    if player_name == default_name:
        player_name = ''            # clear the playername if set to default

    if len(total_amount) == 0:      # if selection moved and text box is empty
        total_amount = default_amount   # set the default value


def clk_enable_inp_amt():
    global pnamebox_active, pnamebox_color, amtbox_active, amtbox_color
    global player_name, total_amount
    
    amtbox_active = True
    amtbox_color = active_color
    pnamebox_active = False
    pnamebox_color = passive_color
    
    if total_amount == default_amount:
        total_amount = ''

    if len(player_name) == 0:
        player_name = default_name


def clk_disable_inp_name_amt():
    global pnamebox_active, pnamebox_color, amtbox_active, amtbox_color
    global player_name, total_amount
    
    amtbox_active = False
    pnamebox_active = False
    pnamebox_color = passive_color
    amtbox_color = passive_color

    if len(player_name) == 0:
        player_name = default_name

    if len(total_amount) == 0:
        total_amount = default_amount


def clk_enable_inp_bet():
    global betbox_active, betbox_color, insuff_amt_flg

    betbox_active = True
    betbox_color = active_color
    
    insuff_amt_flg = False


def clk_disable_inp_bet():
    global betbox_active, betbox_color, curr_bet, insuff_amt_flg

    betbox_active = False
    betbox_color  = passive_color

    if len(curr_bet) == 0:
        curr_bet = default_bet

    insuff_amt_flg = False


def remove_last_entered_char():
    global pnamebox_active, player_name, amtbox_active, total_amount, betbox_active, curr_bet

    if pnamebox_active == True:
        player_name = player_name[:-1]

    if amtbox_active == True:
        total_amount = total_amount[:-1]

    if betbox_active == True:
        curr_bet = curr_bet[:-1]


def gen_stand_event():
    global dealer_card, dealer_count, dealer_count_disp, i, game_buttons_active, player_count
    global game_over_key_active, curr_bet, total_amount

    dealer_card[0] = card_deck[0]
    dealer_count.append(card_value(dealer_card[0]))
    dealer_count_disp = font4.render(str(sum(dealer_count)), True, white)
  
    if sum(player_count) <= 21:
        while sum(dealer_count) < 17:
            dealer_card.append(card_deck[i])
            dealer_count.append(card_value(dealer_card[-1]))

            while sum(dealer_count) > 21:
                try:
                    index_pos = dealer_count.index(11)

                except:
                    index_pos = -1

                if index_pos != -1:
                    dealer_count[index_pos] = 1

                else:
                    break
            
            i += 1

    dealer_count_disp = font4.render(str(sum(dealer_count)), True, white)

    global player_tcount, dealer_tcount
    
    player_tcount = sum(player_count)
    dealer_tcount = sum(dealer_count)
    
    if player_tcount == dealer_tcount:
        total_amount = str(int(total_amount) + int(curr_bet))

    elif player_tcount <= 21 and (dealer_tcount > 21 or dealer_tcount < player_tcount):
        total_amount = str(int(total_amount) + 2 * int(curr_bet))

    
    game_buttons_active  = False
    game_over_key_active = True
    curr_bet = temp_bet


def gen_double_event():
    global curr_bet, curr_bet_disp, player_card, player_count, player_count_disp, i, total_amount
    
    total_amount  = str(int(total_amount) - int(curr_bet)) 
    curr_bet      = str(int(curr_bet) * 2)
    curr_bet_disp = font4.render(curr_bet, True, white)
    player_card.append(card_deck[i])

    player_count.append(card_value(player_card[-1]))

    while sum(player_count) > 21:
        try:
            index_pos = player_count.index(11)

        except:
            index_pos = -1

        if index_pos != -1:
            player_count[index_pos] = 1

        else:
            break

    player_count_disp = font4.render(str(sum(player_count)), True, white)

    i += 1

    gen_stand_event()


def gen_hit_event():
    global player_count, player_card, player_count_disp, i

    if sum(player_count) < 21:
        player_card.append(card_deck[i])
        player_count.append(card_value(player_card[-1]))

        while sum(player_count) > 21:
            try:
                index_pos = player_count.index(11)

            except:
                index_pos = -1

            if index_pos != -1:
                player_count[index_pos] = 1

            else:
                break

        player_count_disp = font4.render(str(sum(player_count)), True, white)
        
        i += 1

    if sum(player_count) > 21:
        gen_stand_event()


def move_icon_n_take_inp():
    global icon_y, name_txt, pname_box, amt_txt, total_amt_box, playicon_box_active, icon_x, restart_flg

    if icon_y >= 210:
        icon_y -= 7             # move the icon 7 pixels at a time such that it
        
        if restart_flg == True:
            icon_x -= 8.75


    elif icon_y < 210:          # stop the icon if y coordinate becomes less than 210
        pygame.draw.rect(screen, pnamebox_color, pname_box, 2)
        pygame.draw.rect(screen, amtbox_color, total_amt_box, 2)
        screen.blit(enter_name, (160, 355))     # draw rectangles for user input
        screen.blit(enter_amount, (160, 395))
        pygame.draw.rect(screen, forest_green, playicon_box)
        screen.blit(play_icon, (360, 450))      # add start match icon

        # add texts to player name box and amount box
        name_txt = font3.render(player_name, True, white)
        screen.blit(name_txt, (pname_box.x + 5, pname_box.y + 5))
        pname_box.w = max(name_txt.get_width() + 10, 200)       # setting size of the box
        
        amount_txt = font3.render(total_amount, True, white)    
        screen.blit(amount_txt, (total_amt_box.x + 5, total_amt_box.y + 5))
        total_amt_box.w = max(amount_txt.get_width() + 10, 200)

        restart_flg = False

        playicon_box_active = True


def config_psetting_move_icon():
    global run_once_flg, player_name, total_amount, pname_txt, playicon_box_active
    global inp_bet_active, config_player_active

    if run_once_flg == True:
        if len(player_name) == 0:
            player_name = default_name

        if len(total_amount) == 0:
            total_amount = default_amount

        pname_txt = font4.render(player_name[:12], True, white)


        playicon_box_active = False
        run_once_flg        = False

    global icon_x, icon_y, betplayicon_box_active

    if icon_y <= 475:                # move the icon to bottom right cornor
        icon_x += 8.75
        icon_y += 7

    elif icon_y > 475:
        playicon_box_active = False
        inp_bet_active = True
        config_player_active = False
        betplayicon_box_active = True


def place_your_bet():
    global place_bet_txt, curr_bet_txt, pname_box, curr_bet_disp, upd_amt_txt, total_amt_box, temp_bet

    screen.blit(back_cards, (131, 100))
    screen.blit(place_bet_txt, (305, 350))
    pygame.draw.rect(screen, betbox_color, place_bet_box, 2)

    curr_bet_txt = font3.render('$'+curr_bet, True, white)
    screen.blit(curr_bet_txt, (place_bet_box.x + 5, place_bet_box.y + 5))
    pname_box.w = max(curr_bet_txt.get_width() + 10, 100)       # setting size of the box

    temp_bet = curr_bet
    curr_bet_disp = font4.render(curr_bet, True, white)
    
    pygame.draw.rect(screen, forest_green, betplayicon_box)
    screen.blit(play_icon, (360, 435))      # add start match icon

    pygame.draw.rect(screen, forest_green, restart_box)
    screen.blit(restart_icon, (5, 512))
    screen.blit(restart_txt,  (9, 576))

    pygame.draw.rect(screen, passive_color, curr_amt_box, 2)
    upd_amt_txt = font2.render('$'+total_amount, True, white)    
    screen.blit(upd_amt_txt, (curr_amt_box.x + 7, curr_amt_box.y + 3))
    total_amt_box.w = max(upd_amt_txt.get_width() + 10, 100)

    global restart_button_active, restart_flg, insuff_amt_flg

    if insuff_amt_flg == True:
        disp_insuff_amt()

    restart_button_active = True
    restart_flg = True



def shuffle_deck_n_strt():
    global dealer_count_disp, player_count_disp, i, betplayicon_box_active, game_ready_active_disp
    global game_buttons_active, total_amount, curr_bet, double_flg

    shuffle(dealer_back_card)
    shuffle(card_deck)

    total_amount = str(int(total_amount) - int(curr_bet))

    dealer_card.extend([dealer_back_card[0], card_deck[1]])
    player_card.extend([card_deck[2], card_deck[3]])

    dealer_count.append(card_value(dealer_card[1]))
    player_count.extend([card_value(player_card[0]), card_value(player_card[1])])

    dealer_count_disp = font4.render(str(sum(dealer_count)), True, white)
    player_count_disp = font4.render(str(sum(player_count)), True, white)

    i = 4

    betplayicon_box_active = False
    game_ready_active_disp = True
    game_buttons_active    = True

    if int(curr_bet) <= int(total_amount):
        double_flg = True

    else:
        double_flg = False


def disp_game_buttons():
    global double_flg

    pygame.draw.rect(screen, forest_green, stand_box)
    screen.blit(stand_icon, (286, 475))
    screen.blit(stand_txt,  (290, 530))

    pygame.draw.rect(screen, forest_green, hit_box)
    screen.blit(hit_icon, (447, 475))
    screen.blit(hit_txt,  (460, 530))
    
    if double_flg == True:
        pygame.draw.rect(screen, forest_green, double_box)
        screen.blit(double_icon, (367, 475))
        screen.blit(double_txt,  (365, 530))


def start_the_game():
    pygame.draw.rect(screen, forest_green, restart_box)
    screen.blit(restart_icon, (5, 512))
    screen.blit(restart_txt,  (9, 576))

    screen.blit(dealer_txt, (5, 100))
    screen.blit(count_txt, (5, 130))
    screen.blit(dealer_count_disp, (65, 130))
    
    screen.blit(pname_txt,  (5, 300))
    screen.blit(bet_txt, (5, 360))
    screen.blit(count_txt, (5, 330))
    screen.blit(player_count_disp, (65, 330))

    screen.blit(curr_bet_disp, (65, 360))

    global upd_amt_txt, total_amt_box

    pygame.draw.rect(screen, passive_color, curr_amt_box, 2)
    upd_amt_txt = font2.render('$'+total_amount, True, white)    
    screen.blit(upd_amt_txt, (curr_amt_box.x + 7, curr_amt_box.y + 3))
    total_amt_box.w = max(upd_amt_txt.get_width() + 10, 100)

    
    for d_card in range(len(dealer_card)):
        screen.blit(dealer_card[d_card], (131 + 65 * d_card, 10))

    for p_card in range(len(player_card)):
        screen.blit(player_card[p_card], (131 + 65 * p_card, 230))


def disp_game_result():
    global player_count, dealer_count

    if player_tcount == dealer_tcount:
        screen.blit(draw_txt, (308, 475))

    elif player_tcount <= 21 and (dealer_tcount > 21 or dealer_tcount < player_tcount):
        screen.blit(win_txt, (328, 475))

    else:
        screen.blit(lose_txt, (322, 475))

    screen.blit(over_continue_txt, (278, 510))


def disp_insuff_amt():
    screen.blit(invalid_bet_txt, (300, 505))
    screen.blit(tamt_less_txt,   (280, 530))


def soft_restart():
    global game_over_key_active, game_ready_active_disp, inp_bet_active
    global betplayicon_box_active, player_count, dealer_count
    global dealer_card, player_card

    game_over_key_active   = False
    game_ready_active_disp = False

    inp_bet_active         = True
    betplayicon_box_active = True

    player_count = []
    dealer_count = []

    dealer_card  = []
    player_card  = []


def hard_restart():
    global game_ready_active_disp, player_count, dealer_count, player_card, dealer_card
    global curr_bet, player_name, total_amount, restart_button_active, inp_name_amt_active
    global run_once_flg

    run_once_flg = True

    player_name  = default_name
    curr_bet     = default_bet
    total_amount = default_amount

    game_ready_active_disp = False

    inp_name_amt_active    = True

    player_count = []
    dealer_count = []

    dealer_card  = []
    player_card  = []

    restart_button_active = False


# Variable indicates game is running which allows to run loop infinitely
running = True


# Iterate loop until the game is running
while running:
    clock.tick(fps)             # setting the frame rate
    
    screen.fill(forest_green)
    place_icon(icon_x, icon_y)

    for event in pygame.event.get():        # Loop through input events
        if event.type == pygame.QUIT:       # if quit is pressed
            running = False                 # terminate the loop
    
        # setting keyboard events
        if event.type == pygame.KEYDOWN:
            # Remove the last entered character from the text box if active
            if event.key == pygame.K_BACKSPACE:     # backspace key events
                remove_last_entered_char()
                
            # Add characters to the text boxes if the text box is active
            if pnamebox_active == True:
                player_name += event.unicode

            elif amtbox_active == True:
                if event.unicode.isdigit():     # add only if it is a digit
                    total_amount += event.unicode

            elif betbox_active == True:
                if event.unicode.isdigit():
                    curr_bet += event.unicode

            elif loading_flag == True:
                if time.time() > seconds + 1.5:
                    inp_name_amt_active = True
                    loading_flag      = False

            elif game_over_key_active == True:
                soft_restart()



        # Setting mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if button is clicks inside any of the text boxes
            if inp_name_amt_active == True:
                if pname_box.collidepoint(event.pos):
                    clk_enable_inp_name()

                elif total_amt_box.collidepoint(event.pos):   # for total amount text box
                    clk_enable_inp_amt()

                else:
                    clk_disable_inp_name_amt()

            elif inp_bet_active == True: 
                if place_bet_box.collidepoint(event.pos):
                    clk_enable_inp_bet()

                else:
                    clk_disable_inp_bet()


            if playicon_box_active == True:
                if playicon_box.collidepoint(event.pos):    # if button is pressed on play icon
                    clk_disable_inp_name_amt()
                    config_player_active = True
                    inp_name_amt_active = False

            elif betplayicon_box_active == True:
                if betplayicon_box.collidepoint(event.pos):
                    if int(total_amount) >= int(curr_bet):
                        inp_bet_active = False
                        clk_disable_inp_bet()
                        shuffle_deck_n_strt()

                    else:
                        insuff_amt_flg = True
                        inp_bet_active = True

            elif game_buttons_active == True:
                if stand_box.collidepoint(event.pos):
                    gen_stand_event()
                
                elif hit_box.collidepoint(event.pos):
                    gen_hit_event()
                
                if double_flg == True:
                    if double_box.collidepoint(event.pos):
                        gen_double_event()
                
            
            if restart_button_active == True:
                if restart_box.collidepoint(event.pos):
                    hard_restart()

    if loading_flag == True:
        if time.time() < seconds + 1:
            disp_loading_txt()
        
        elif time.time() > seconds + 1.3:
            disp_continue_txt()


    elif inp_name_amt_active == True:
        move_icon_n_take_inp()

    elif config_player_active == True:
        config_psetting_move_icon()

    elif inp_bet_active == True:
        place_your_bet()

    elif game_ready_active_disp == True:
        start_the_game()

        if game_buttons_active:
            disp_game_buttons()

        else:
            disp_game_result()

    pygame.display.update()             # update the display (game window)
