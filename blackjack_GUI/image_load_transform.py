import pygame

# icon load
icon      = pygame.image.load('icons/blackjack-icon.png')      # icon for title bar and loading screen
play_icon = pygame.image.load('icons/play-icon.png')           # game icon always on screen


# Deck Image Load
spade_A     = pygame.image.load('cards/AS.png')
spade_2     = pygame.image.load('cards/2S.png')
spade_3     = pygame.image.load('cards/3S.png')
spade_4     = pygame.image.load('cards/4S.png')
spade_5     = pygame.image.load('cards/5S.png')
spade_6     = pygame.image.load('cards/6S.png')
spade_7     = pygame.image.load('cards/7S.png')
spade_8     = pygame.image.load('cards/8S.png')
spade_9     = pygame.image.load('cards/9S.png')
spade_10    = pygame.image.load('cards/10S.png')
spade_J     = pygame.image.load('cards/JS.png')
spade_Q     = pygame.image.load('cards/QS.png')
spade_K     = pygame.image.load('cards/KS.png')

diamond_A   = pygame.image.load('cards/AD.png')
diamond_2   = pygame.image.load('cards/2D.png')
diamond_3   = pygame.image.load('cards/3D.png')
diamond_4   = pygame.image.load('cards/4D.png')
diamond_5   = pygame.image.load('cards/5D.png')
diamond_6   = pygame.image.load('cards/6D.png')
diamond_7   = pygame.image.load('cards/7D.png')
diamond_8   = pygame.image.load('cards/8D.png')
diamond_9   = pygame.image.load('cards/9D.png')
diamond_10  = pygame.image.load('cards/10D.png')
diamond_J   = pygame.image.load('cards/JD.png')
diamond_Q   = pygame.image.load('cards/QD.png')
diamond_K   = pygame.image.load('cards/KD.png')

heart_A     = pygame.image.load('cards/AH.png')
heart_2     = pygame.image.load('cards/2H.png')
heart_3     = pygame.image.load('cards/3H.png')
heart_4     = pygame.image.load('cards/4H.png')
heart_5     = pygame.image.load('cards/5H.png')
heart_6     = pygame.image.load('cards/6H.png')
heart_7     = pygame.image.load('cards/7H.png')
heart_8     = pygame.image.load('cards/8H.png')
heart_9     = pygame.image.load('cards/9H.png')
heart_10    = pygame.image.load('cards/10H.png')
heart_J     = pygame.image.load('cards/JH.png')
heart_Q     = pygame.image.load('cards/QH.png')
heart_K     = pygame.image.load('cards/KH.png')

club_A      = pygame.image.load('cards/AC.png')
club_2      = pygame.image.load('cards/2C.png')
club_3      = pygame.image.load('cards/3C.png')
club_4      = pygame.image.load('cards/4C.png')
club_5      = pygame.image.load('cards/5C.png')
club_6      = pygame.image.load('cards/6C.png')
club_7      = pygame.image.load('cards/7C.png')
club_8      = pygame.image.load('cards/8C.png')
club_9      = pygame.image.load('cards/9C.png')
club_10     = pygame.image.load('cards/10C.png')
club_J      = pygame.image.load('cards/JC.png')
club_Q      = pygame.image.load('cards/QC.png')
club_K      = pygame.image.load('cards/KC.png')

spade_A     = pygame.transform.smoothscale(spade_A,     (132, 203))
spade_2     = pygame.transform.smoothscale(spade_2,     (132, 203))
spade_3     = pygame.transform.smoothscale(spade_3,     (132, 203))
spade_4     = pygame.transform.smoothscale(spade_4,     (132, 203))
spade_5     = pygame.transform.smoothscale(spade_5,     (132, 203))
spade_6     = pygame.transform.smoothscale(spade_6,     (132, 203))
spade_7     = pygame.transform.smoothscale(spade_7,     (132, 203))
spade_8     = pygame.transform.smoothscale(spade_8,     (132, 203))
spade_9     = pygame.transform.smoothscale(spade_9,     (132, 203))
spade_10    = pygame.transform.smoothscale(spade_10,    (132, 203))
spade_J     = pygame.transform.smoothscale(spade_J,     (132, 203))
spade_Q     = pygame.transform.smoothscale(spade_Q,     (132, 203))
spade_K     = pygame.transform.smoothscale(spade_K,     (132, 203))

diamond_A   = pygame.transform.smoothscale(diamond_A,   (132, 203))
diamond_2   = pygame.transform.smoothscale(diamond_2,   (132, 203))
diamond_3   = pygame.transform.smoothscale(diamond_3,   (132, 203))
diamond_4   = pygame.transform.smoothscale(diamond_4,   (132, 203))
diamond_5   = pygame.transform.smoothscale(diamond_5,   (132, 203))
diamond_6   = pygame.transform.smoothscale(diamond_6,   (132, 203))
diamond_7   = pygame.transform.smoothscale(diamond_7,   (132, 203))
diamond_8   = pygame.transform.smoothscale(diamond_8,   (132, 203))
diamond_9   = pygame.transform.smoothscale(diamond_9,   (132, 203))
diamond_10  = pygame.transform.smoothscale(diamond_10,  (132, 203))
diamond_J   = pygame.transform.smoothscale(diamond_J,   (132, 203))
diamond_Q   = pygame.transform.smoothscale(diamond_Q,   (132, 203))
diamond_K   = pygame.transform.smoothscale(diamond_K,   (132, 203))

heart_A     = pygame.transform.smoothscale(heart_A,     (132, 203))
heart_2     = pygame.transform.smoothscale(heart_2,     (132, 203))
heart_3     = pygame.transform.smoothscale(heart_3,     (132, 203))
heart_4     = pygame.transform.smoothscale(heart_4,     (132, 203))
heart_5     = pygame.transform.smoothscale(heart_5,     (132, 203))
heart_6     = pygame.transform.smoothscale(heart_6,     (132, 203))
heart_7     = pygame.transform.smoothscale(heart_7,     (132, 203))
heart_8     = pygame.transform.smoothscale(heart_8,     (132, 203))
heart_9     = pygame.transform.smoothscale(heart_9,     (132, 203))
heart_10    = pygame.transform.smoothscale(heart_10,    (132, 203))
heart_J     = pygame.transform.smoothscale(heart_J,     (132, 203))
heart_Q     = pygame.transform.smoothscale(heart_Q,     (132, 203))
heart_K     = pygame.transform.smoothscale(heart_K,     (132, 203))

club_A      = pygame.transform.smoothscale(club_A,      (132, 203))
club_2      = pygame.transform.smoothscale(club_2,      (132, 203))
club_3      = pygame.transform.smoothscale(club_3,      (132, 203))
club_4      = pygame.transform.smoothscale(club_4,      (132, 203))
club_5      = pygame.transform.smoothscale(club_5,      (132, 203))
club_6      = pygame.transform.smoothscale(club_6,      (132, 203))
club_7      = pygame.transform.smoothscale(club_7,      (132, 203))
club_8      = pygame.transform.smoothscale(club_8,      (132, 203))
club_9      = pygame.transform.smoothscale(club_9,      (132, 203))
club_10     = pygame.transform.smoothscale(club_10,     (132, 203))
club_J      = pygame.transform.smoothscale(club_J,      (132, 203))
club_Q      = pygame.transform.smoothscale(club_Q,      (132, 203))
club_K      = pygame.transform.smoothscale(club_K,      (132, 203))


# Back Cards
red_back    = pygame.image.load('cards/red_back.png')
purple_back = pygame.image.load('cards/purple_back.png')
yellow_back = pygame.image.load('cards/yellow_back.png')
gray_back   = pygame.image.load('cards/gray_back.png')
blue_back   = pygame.image.load('cards/blue_back.png')
green_back  = pygame.image.load('cards/green_back.png')

red_back    = pygame.transform.smoothscale(red_back,    (132, 203))
purple_back = pygame.transform.smoothscale(purple_back, (132, 203))
yellow_back = pygame.transform.smoothscale(yellow_back, (132, 203))
gray_back   = pygame.transform.smoothscale(gray_back,   (132, 203))
blue_back   = pygame.transform.smoothscale(blue_back,   (132, 203))
green_back  = pygame.transform.smoothscale(green_back,  (132, 203))

back_cards = pygame.image.load('cards/back_cards.png')
back_cards = pygame.transform.smoothscale(back_cards, (538, 260))


# gameplay icons
restart_icon = pygame.image.load('icons/restart-icon.png')
stand_icon   = pygame.image.load('icons/stand-icon.png')
double_icon  = pygame.image.load('icons/double-icon.png')
hit_icon     = pygame.image.load('icons/hit-icon.png')

stand_icon   = pygame.transform.smoothscale(stand_icon,  (48, 48))
hit_icon     = pygame.transform.smoothscale(hit_icon,    (48, 48))
double_icon  = pygame.transform.smoothscale(double_icon, (48, 48))
