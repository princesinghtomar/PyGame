#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import math
import config
import random
import time
from pygame import mixer

# game start

pygame.init()

# this creates the screen of the game

message_if_2_died = config.message_if_2_died
message_if_1_died = config.message_if_1_died
message_if_both_died = config.message_if_both_died
message_if_both_alive = config.message_if_both_alive
message_for_won1 = config.message_for_won1
message_for_won2 = config.message_for_won2

font_style = config.font_style

color = config.color

background_color = config.background_color
other_bg_color = config.other_bg_color

screen_x = 900
screen_y = 770

screen = pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()
# BackgroundS

backgroundimage1 = 'background.png'
other_screen_image = 'background.png'
background = pygame.image.load(backgroundimage1)
background2 = pygame.image.load(other_screen_image)

# Background Sound

background_music = 'background.wav'
laser_music = 'laser.wav'
explosion_music = 'explosion.wav'
mixer.music.load(background_music)
mixer.music.play(-1)
bullet_Sound = mixer.Sound(laser_music)

# -------------------------------------------title and icon

game_icon = 'icon.png'
pygame.display.set_caption('Cross it')
icon = pygame.image.load(game_icon)
pygame.display.set_icon(icon)

# ----------------------------------------------------score

score_value1 = 0
text_score1_X = 40
text_score1_Y = 720

font = pygame.font.Font(font_style, 32)

score_value2 = 0
text_score2_X = 670
text_score2_Y = 720


def show_score1(x, y):
    score = font.render('Score1 : ' + str(score_value1), True, color)
    screen.blit(score, (x, y))


def show_score2(x, y):
    score = font.render('Score2 : ' + str(score_value2), True, color)
    screen.blit(score, (x, y))


# --------------------------------------------------timer

time_value = 40000
text_time_X = 650
text_time_Y = 10


# color = (255,165,0)

def show_death1(x, y):
    death1 = font.render(str(message_if_1_died), True, color)
    screen.blit(death1, (x, y))


def show_death2(x, y):
    death2 = font.render(str(message_if_2_died), True, color)
    screen.blit(death2, (x, y))


def show_death3(x, y):
    death3 = font.render(str(message_if_both_died), True, color)
    screen.blit(death3, (x, y))


def show_death4(x, y):
    death4 = font.render(str(message_if_both_alive), True, color)
    screen.blit(death4, (x, y))


def show_time(x, y):
    time = font.render('Time Left : ' + str(time_value), True, color)
    screen.blit(time, (x, y))


# --------------------------------------------------level

def show_level(x, y):
    level_ = font.render('Level: ' + str(level), True, color)
    screen.blit(level_, (x, y))


# ----------------------------------------------------end

def show_end(x, y):
    end = font.render('End', True, color)
    screen.blit(end, (x, y))


# --------------------------------------------final_winner

def show_final_winner(x, y):
    font
    final_winner_ = font.render(
        message_for_won1 +
        final_winner +
        message_for_won2,
        True,
        color)
    screen.blit(final_winner_, (x, y))


# ----------------------------------------------------score

def show_score(x, y):
    score_ = font.render('player1 : ' + str(score_value1) +
                         '              ' + 'player2 : ' +
                         str(score_value2), True, color)
    screen.blit(score_, (x, y))


# ----------------------------------------------------start

def show_start(x, y):
    start = font.render('1       Start      2', True, color)
    screen.blit(start, (x, y))


# ---------------------------------------------start_screen

def show_start_screens(x, y):
    starts = font.render('Press Space to start the Game', True, color)
    screen.blit(starts, (x, y))


def show_start_screenq(x, y):
    startq = font.render('Press Q to exit the Game', True, color)
    screen.blit(startq, (x, y))


# ---------------------------------------level_change_screen

def show_next_level(x, y):
    next_level = font.render('Press Space to begin Next Level', True,
                             color)
    screen.blit(next_level, (x, y))


# --------------------------------------------exit_screens

def show_exit_screens(x, y):
    starts = font.render('Press Space to start the Game', True, color)
    screen.blit(starts, (x, y))


def show_exit_screenq(x, y):
    startq = font.render('Press Q to exit the Game', True, color)
    screen.blit(startq, (x, y))


def show_winner(x, y):
    winner1 = font.render('Winner of this Level :', True, color)
    winner = font.render('Player1 : ' + status1 + '   Player2 :' +
                         status2, True, color)
    screen.blit(winner1, (x, y))
    screen.blit(winner, (x, y))


# ---------------------------------------------------scoreup

scoreupx = random.randint(70, 800)
scoreupy = random.randint(12, 700)
scoreup = pygame.image.load('scoreup.png')
scoreuptaken = False


def score_up(x, y):
    screen.blit(scoreup, (x, y))

# ---------------------------------------------------player1 ship


player1_image = 'ship.png'
player2_image = 'ship2.png'
player1Img = pygame.image.load(player1_image)
player1X = 280
player1Y = 700
player1x_change = 0
player1y_change = 0

# --------------------------------------------------player1 ship

player2Img = pygame.image.load(player2_image)
player2X = 470
player2Y = 700
player2x_change = 0
player2y_change = 0

# ---------------------------------------------------asteroid

asteroidImg = pygame.image.load('asteroid.png')
asteroidX = random.randint(300, 1200)
asteroidY = random.randint(-100, 300)
asteroidX_change = -0.3
asteroidY_change = 0.3


def show_asteroid(x, y):
    screen.blit(asteroidImg, (x, y))


# function for showing on screen

def player1(x, y):
    screen.blit(player1Img, (x, y))


def player2(x, y):
    screen.blit(player2Img, (x, y))


# ---------------------------------laser as obstcles

laserImg = pygame.image.load('laser.png')

# list no. 1

laser11X = random.randint(70, 900)
laser11Y = 505
laser14X = random.randint(70, 900)
laser14Y = 505
laser16X = random.randint(70, 900)
laser16Y = 505
laser1x_change = 0.6

# list no. 2

laser22X = 210
laser22Y = 365
laser25X = 630
laser25Y = 365
laser2x_change = 0.7

# list no. 3

laser31X = 70
laser31Y = 225
laser34X = 490
laser34Y = 225
laser3x_change = 0.8

# list no. 4

laser41X = 70
laser41Y = 85
laser4x_change = 0.9

# list no. 5

laser51X = random.randint(70, 900)
laser51Y = 645
laser52X = random.randint(70, 900)
laser52Y = 645
laser5x_change = 0.5


# function on showing on screen

def laser(x, y):
    screen.blit(laserImg, (x, y))


# ----------------------------------------laser gun

gunImg = pygame.image.load('gun.png')
gun1X = 0
gun1Y = 479  # 470 + 9 for laser to move perfectly

# gun 2

gun2X = 0
gun2Y = 339  # 470 + 9 for laser to move perfectly

# gun 3

gun3X = 0
gun3Y = 199  # 470 + 9 for laser to move perfectly

# gun 4

gun4X = 0
gun4Y = 59  # 470 + 9 for laser to move perfectly

# gun 5

gun5X = 0
gun5Y = 619


# function on showing on screen

def gun(x, y):
    screen.blit(gunImg, (x, y))


# -----------------------------------------obstacles here

obstacleImg = pygame.image.load('wall.png')

# no. 2

obstacle21X = random.randint(0, 900)
obstacle21Y = 280

# no. 3

obstacle31X = random.randint(0, 900)
obstacle31Y = 140
obstaclex_change = 0


# function for showing on screen

def obstacle(x, y):
    screen.blit(obstacleImg, (x, y))


# ----------------------------------------collision effect

def iscollision(
    bulletX,
    bulletY,
    playerX,
    playerY,
):
    distance = math.sqrt(math.pow(bulletX - playerX - 35, 2) +
                         math.pow(bulletY - playerY - 35, 2))
    if distance < 30:
        explosion_Sound = mixer.Sound('explosion.wav')
        explosion_Sound.play()
        return True
    else:
        return False


def iscollisionobstacle(
    bulletX,
    bulletY,
    playerX,
    playerY,
):
    distance = math.sqrt(math.pow(bulletX - playerX, 2) +
                         math.pow(bulletY - playerY, 2))
    if distance < 30:
        explosion_Sound = mixer.Sound('explosion.wav')
        explosion_Sound.play()
        return True
    else:
        return False


def istakingscoreup(
    bulletX,
    bulletY,
    playerX,
    playerY,
):
    distance = math.sqrt(math.pow(bulletX - playerX, 2) +
                         math.pow(bulletY - playerY, 2))
    if distance < 30:
        explosion_sound1 = mixer.Sound('powerup.ogg')
        explosion_sound1.play()
        return True
    else:
        return False


# score_variables

laser1pass1 = True
laser1pass2 = True
laser2pass1 = True
laser2pass2 = True
laser3pass1 = True
laser3pass2 = True
laser4pass1 = True
laser4pass2 = True
laser5pass1 = True
laser5pass2 = True
obstacle21pass1 = True
obstacle21pass2 = True
obstacle31pass1 = True
obstacle31pass2 = True
asteroidpass1 = True
asteroidpass2 = True

# game loop

start_screen = True
exit_screen = False
final_screen = False
run = True
count = 0
level = 1
player1life = True
player2life = True
final_winner = 'player1'
status1 = 'Loser'
status2 = 'Loser'

# background_color = (0,0,0)###
# other_bg_color = (0,255,0)###

while run:

    seconds = pygame.time.get_ticks()
    time_a = seconds % 2000
    if time_a == 0:
        score_value1 -= 1
        score_value2 -= 1

    # background color next line

    screen.fill(color)
    screen.blit(background, (0, 0))

    if not player1life:
        player1x_change = 0
        player1y_change = 0
        player1(900, 770)

    if not player2life:
        player2x_change = 0
        player2y_change = 0
        player2(900, 770)

    while start_screen:
        screen.fill(color)
        screen.blit(background2, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_screen = False
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    start_screen = False
                    run = False

        show_start_screens(200, 270)
        show_start_screenq(250, 370)
        if event.type == pygame.KEYUP:

            if event.key == ord('q') or event.key == ord('Q'):
                start_sreen = False
                run = False

            if event.key == pygame.K_SPACE:
                start_screen = False
                run = True

        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # here we are checking the events on the keyboard

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_LEFT and player1life:

            # what to do if left arrow key is pressed

            player1x_change = -1

        if event.key == ord('a') and player2life:

            # what to do if left arrow key is pressed

            player2x_change = -1

        if event.key == pygame.K_RIGHT and player1life:

            # what to do if right arrow key is pressed

            player1x_change = 1

        if event.key == ord('d') and player2life:

            # what to do if right arrow key is pressed

            player2x_change = 1

        if event.key == pygame.K_UP and player1life:

            # what to do if right arrow key is pressed

            player1y_change = -1.3

        if event.key == ord('w') and player2life:

            # what to do if right arrow key is pressed

            player2y_change = -1.3

        if event.key == pygame.K_DOWN and player1life:

            # what to do if right arrow key is pressed

            player1y_change = 1.3

        if event.key == ord('s') and player2life:

            # what to do if right arrow key is pressed

            player2y_change = 1.3

    if event.type == pygame.KEYUP:

        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT\
                and player1life:
            player1x_change = 0

        if event.key == ord('a') or event.key == ord('d') and player2life:
            player2x_change = 0

        if event.key == pygame.K_UP or event.key == pygame.K_DOWN \
                and player1life:
            player1y_change = 0

        if event.key == ord('w') or event.key == ord('s') and player2life:
            player2y_change = 0

    # -------------------------------------------------player1 here

    player1X += player1x_change
    player2X += player2x_change
    player1Y += player1y_change
    player2Y += player2y_change
    asteroidX += asteroidX_change
    asteroidY += asteroidY_change

    # boundary of player1

    if player1X < 70:
        player1X = 70

    if player1X > 840:
        player1X = 840

    if player1Y > 700:
        player1Y = 700

    if player1Y < 0:
        player1Y = 0

    # boundary of player2

    if player2X < 70:
        player2X = 70

    if player2X > 840:
        player2X = 840

    if player2Y > 700:
        player2Y = 700

    if player2Y < 0:
        player2Y = 0

    # -------------------------------------------------------start and end

    show_level(10, 10)
    show_start(310, 720)
    show_end(410, 10)

    # ----------------------------------------------------lasers here
    # no. 1

    laser11X += laser1x_change
    if laser11X > 900:
        laser11X = 70
        bullet_Sound.play()

    if player1life:
        collision = iscollision(laser11X, laser11Y, player1X, player1Y)
        if collision:
            player1X = 395
            player1Y = 700
            score_value1 = score_value1 - 2
            player1life = False

    if player2life:
        collision = iscollision(laser11X, laser11Y, player2X, player2Y)
        if collision:
            player2X = 395
            player2Y = 700
            score_value2 = score_value2 - 2
            player2life = False

    laser14X += laser1x_change
    if laser14X > 900:
        laser14X = 70
        bullet_Sound.play()

    if player1life:
        collision = iscollision(laser14X, laser14Y, player1X, player1Y)
        if collision:
            player1X = 395
            player1Y = 700
            score_value1 = score_value1 - 2
            player1life = False

    if player2life:
        collision = iscollision(laser14X, laser14Y, player2X, player2Y)
        if collision:
            player2X = 395
            player2Y = 700
            score_value2 = score_value2 - 2
            player2life = False

    laser16X += laser1x_change
    if laser16X > 900:
        laser16X = 70
        bullet_Sound.play()

    if player1life:
        collision = iscollision(laser16X, laser16Y, player1X, player1Y)
        if collision:
            player1X = 395
            player1Y = 700
            score_value1 = score_value1 - 2
            player1life = False

    if player2life:
        collision = iscollision(laser16X, laser16Y, player2X, player2Y)
        if collision:
            player2X = 395
            player2Y = 700
            score_value2 = score_value2 - 2
            player2life = False

        # no. 2

    laser22X += laser2x_change
    if laser22X > 900:
        laser22X = 70
        bullet_Sound.play()

    if player1life:
        collision = iscollision(laser22X, laser22Y, player1X, player1Y)
        if collision:
            player1X = 395
            player1Y = 700
            score_value1 = score_value1 - 2
            player1life = False

    if player2life:
        collision = iscollision(laser22X, laser22Y, player2X, player2Y)
        if collision:
            player2X = 395
            player2Y = 700
            score_value2 = score_value2 - 2
            player2life = False

    laser25X += laser2x_change
    if laser25X > 900:
        laser25X = 70
        bullet_Sound.play()

    if player1life:
        collision = iscollision(laser25X, laser25Y, player1X, player1Y)
        if collision:
            player1X = 395
            player1Y = 700
            score_value1 = score_value1 - 2
            player1life = False

    if player2life:
        collision = iscollision(laser25X, laser25Y, player2X, player2Y)
        if collision:
            player2X = 395
            player2Y = 700
            score_value2 = score_value2 - 2
            player2life = False

        # no. 3

    laser31X += laser3x_change
    if laser31X > 900:
        laser31X = 70
        bullet_Sound.play()

    if player1life:
        collision = iscollision(laser31X, laser31Y, player1X, player1Y)
        if collision:
            player1X = 395
            player1Y = 700
            score_value1 = score_value1 - 2
            player1life = False

    if player2life:
        collision = iscollision(laser31X, laser31Y, player2X, player2Y)
        if collision:
            player2X = 395
            player2Y = 700
            score_value2 = score_value2 - 2
            player2life = False

    laser34X += laser3x_change
    if laser34X > 900:
        laser34X = 70
        bullet_Sound.play()

    if player1life:
        collision = iscollision(laser34X, laser34Y, player1X, player1Y)
        if collision:
            player1X = 395
            player1Y = 700
            score_value1 = score_value1 - 2
            player1life = False

    if player2life:
        collision = iscollision(laser34X, laser34Y, player2X, player2Y)
        if collision:
            player2X = 395
            player2Y = 700
            score_value2 = score_value2 - 2
            player2life = False

        # no. 4

    laser41X += laser4x_change
    if laser41X > 900:
        laser41X = 70
        bullet_Sound.play()

    if player1life:
        collision = iscollision(laser41X, laser41Y, player1X, player1Y)
        if collision:
            player1X = 395
            player1Y = 700
            score_value1 = score_value1 - 2
            player1life = False

    if player2life:
        collision = iscollision(laser41X, laser41Y, player2X, player2Y)
        if collision:
            player2X = 395
            player2Y = 700
            score_value2 = score_value2 - 2
            player2life = False

        # no. 5

    laser51X += laser5x_change
    if laser51X > 900:
        laser51X = 70
        bullet_Sound.play()

    if player1life:
        collision = iscollision(laser51X, laser51Y, player1X, player1Y)
        if collision:
            player1X = 395
            player1Y = 700
            score_value1 = score_value1 - 2
            player1life = False

    if player2life:
        collision = iscollision(laser51X, laser51Y, player2X, player2Y)
        if collision:
            player2X = 395
            player2Y = 700
            score_value2 = score_value2 - 2
            player2life = False

    laser52X += laser5x_change
    if laser52X > 900:
        laser52X = 70
        bullet_Sound.play()

    if player1life:
        collision = iscollision(laser52X, laser52Y, player1X, player1Y)
        if collision:
            player1X = 395
            player1Y = 700
            score_value1 = score_value1 - 2
            player1life = False

    if player2life:
        collision = iscollision(laser52X, laser52Y, player2X, player2Y)
        if collision:
            player2X = 395
            player2Y = 700
            score_value2 = score_value2 - 2
            player2life = False

    # ------------------------------lasers

        # no. 1

    laser(laser11X, laser11Y)
    laser(laser14X, laser14Y)
    laser(laser16X, laser16Y)

    # no. 2

    laser(laser22X, laser22Y)
    laser(laser25X, laser25Y)

    # no. 3

    laser(laser31X, laser31Y)
    laser(laser34X, laser34Y)

    # no. 4

    laser(laser41X, laser41Y)

    # no. 5

    laser(laser51X, laser51Y)
    laser(laser52X, laser52Y)

    # ------------------------------guns

    gun(gun1X, gun1Y)
    gun(gun2X, gun2Y)
    gun(gun3X, gun3Y)
    gun(gun4X, gun4Y)
    gun(gun5X, gun5Y)
    # ------------------------------scoreup

    if not scoreuptaken:
        score_up(scoreupx, scoreupy)

    if not scoreuptaken:
        if player1life:
            collision = istakingscoreup(scoreupx, scoreupy, player1X, player1Y)
            if collision:
                while not scoreuptaken:
                    score_value1 = score_value1 + 40
                    scoreuptaken = True

        if player2life:
            collision = istakingscoreup(scoreupx, scoreupy, player2X, player2Y)
            if collision:
                while not scoreuptaken:
                    score_value2 = score_value2 + 40
                    scoreuptaken = True

    # ------------------------------obstacles

    show_asteroid(asteroidX, asteroidY)
    if player1life:
        collision = iscollisionobstacle(asteroidX, asteroidY, player1X,
                                        player1Y)
        if collision:
            player1X = 395
            player1Y = 700
            score_value1 = score_value1 - 10
            player1life = False

    if player2life:
        collision = iscollisionobstacle(asteroidX, asteroidY, player2X,
                                        player2Y)
        if collision:
            player2X = 395
            player2Y = 700
            score_value2 = score_value2 - 5
            player2life = False

    # no. 2

    obstacle(obstacle21X, obstacle21Y)
    if player1life:
        collision = iscollisionobstacle(obstacle21X, obstacle21Y, player1X,
                                        player1Y)
        if collision:
            player1X = 395
            player1Y = 700
            score_value1 = score_value1 - 5
            player1life = False

    if player2life:
        collision = iscollisionobstacle(obstacle21X, obstacle21Y, player2X,
                                        player2Y)
        if collision:
            player2X = 395
            player2Y = 700
            score_value2 = score_value2 - 5
            player2life = False

    # no. 3

    obstacle(obstacle31X, obstacle31Y)
    if player1life:
        collision = iscollisionobstacle(obstacle31X, obstacle31Y, player1X,
                                        player1Y)
        if collision:
            player1X = 395
            player1Y = 700
            score_value1 = score_value1 - 5
            player1life = False

    if player2life:
        collision = iscollisionobstacle(obstacle31X, obstacle31Y, player2X,
                                        player2Y)
        if collision:
            player2X = 395
            player2Y = 700
            score_value2 = score_value2 - 5
            player2life = False

    # player_score

    if player1Y > 630 and player1Y < 660 and laser1pass1 \
            and player1life:
        score_value1 += 10
        laser1pass1 = False

    if player1Y > 490 and player1Y < 520 and laser2pass1 \
            and player1life:
        score_value1 += 10
        laser2pass1 = False

    if player1Y > 350 and player1Y < 380 and laser3pass1 \
            and player1life:
        score_value1 += 10
        laser3pass1 = False

    if player1Y > 210 and player1Y < 240 and laser4pass1 \
            and player1life:
        score_value1 += 10
        laser4pass1 = False

    if player1Y > 70 and player1Y < 100 and laser5pass1 and player1life:
        score_value1 += 10
        laser5pass1 = False

    if player1Y > obstacle21Y - 15 and player1Y < obstacle21Y + 15 \
            and obstacle21pass1 and player1life:
        score_value1 += 5
        obstacle21pass1 = False

    if player1Y > obstacle31Y - 15 and player1Y < obstacle31Y + 15 \
            and obstacle31pass1 and player1life:
        score_value1 += 5
        obstacle31pass1 = False

    if player1Y < asteroidY - 15 and player1Y < asteroidY + 15 \
            and asteroidpass1 and player1life:
        score_value1 += 15
        asteroidpass1 = False

    if player2Y > 630 and player2Y < 660 and laser1pass2 \
            and player2life:
        score_value2 += 10
        laser1pass2 = False

    if player2Y > 490 and player2Y < 520 and laser2pass2 \
            and player2life:
        score_value2 += 10
        laser2pass2 = False

    if player2Y > 350 and player2Y < 380 and laser3pass2 \
            and player2life:
        score_value2 += 10
        laser3pass2 = False

    if player2Y > 210 and player2Y < 240 and laser4pass2 \
            and player2life:
        score_value2 += 10
        laser4pass2 = False

    if player2Y < 70 and player2Y < 100 and laser5pass2 and player2life:
        score_value2 += 10
        laser5pass2 = False

    if player2Y > obstacle21Y - 15 and player2Y < obstacle21Y + 15 \
            and obstacle21pass2 and player2life:
        score_value2 += 5
        obstacle21pass2 = False

    if player2Y > obstacle31Y - 15 and player2Y < obstacle31Y + 15 \
            and obstacle31pass2 and player2life:
        score_value2 += 5
        obstacle31pass2 = False

    if player2Y > asteroidY - 15 and player2Y < asteroidY + 15 \
            and asteroidpass2 and player2life:
        score_value2 += 15
        asteroidpass2 = False

    # player1

    if player1life:
        player1(player1X, player1Y)

    if player2life:
        player2(player2X, player2Y)

    # ---------------------------------------update your screen

    show_score1(text_score1_X, text_score1_Y)
    show_score2(text_score2_X, text_score2_Y)
    count = count + 2

    # -----------------------------------score_value = count

    show_time(text_time_X, text_time_Y)
    time_value = time_value - 1

    if time_value == 0 or not player1life and not player2life:
        exit_screen = True
        status1 = 'Loser'
        status2 = 'Loser'

    if player1Y == 0 and player2Y == 0:
        exit_screen = True
        score_value1 += 10
        score_value2 += 10
        status1 = 'Tie'
        status2 = 'Tie'

    if player1Y == 0:
        exit_screen = True
        score_value1 = score_value1 + 15
        status1 = 'Winner'

    if player2Y == 0:
        exit_screen = True
        score_value2 += 15
        status2 = 'Winner'

    if exit_screen:
        level += 1

    if level == 7:
        if score_value1 > score_value2:
            final_winner = 'player1'
        else:
            if score_value2 > score_value1:
                final_winner = 'player2'

            if score_value1 == score_value2:
                final_winner = 'Tie'

        final_screen = True
        while final_screen:
            screen.fill(background_color)
            screen.blit(background2, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    final_screen = False
                    exit_screen = False
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        exit_screen = False
                        final_screen = False
                        run = False

                    if event.key == pygame.K_SPACE:
                        exit_screen = False
                        run = True
                        final_screen = False
                        player1X = 280
                        player1Y = 700
                        player2X = 470
                        player2Y = 700
                        player1life = True
                        player2life = True
                        score_value1 = 0
                        score_value2 = 0
                        time_value = 40000
                        scoreuptaken = False
                        scoreupx = random.randint(70, 800)
                        scoreupy = random.randint(12, 700)
                        asteroidX = random.randint(300, 1200)
                        asteroidY = random.randint(-100, 300)
                        status1 = 'Loser'
                        status2 = 'Loser'
                        player1x_change = 0
                        player1y_change = 0
                        player2x_change = 0
                        player2y_change = 0
                        obstacle21X = random.randint(70, 830)
                        obstacle31X = random.randint(70, 830)
                        laser1x_change = 0.6
                        laser3x_change = 0.7
                        laser2x_change = 0.8
                        laser4x_change = 0.9
                        laser5x_change = 0.5
                        level = 1

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_q:
                    final_sreen = False
                    exit_screen = False
                    run = False

                if event.key == pygame.K_SPACE:
                    final_screen = False
                    exit_screen = False
                    run = True
                    player1X = 280
                    player1Y = 700
                    player2X = 470
                    player2Y = 700
                    player1life = True
                    player2life = True
                    time_value = 40000
                    scoreuptaken = False
                    scoreupx = random.randint(70, 800)
                    scoreupy = random.randint(12, 700)
                    asteroidX = random.randint(300, 1200)
                    asteroidY = random.randint(-100, 300)
                    status1 = 'Loser'
                    status2 = 'Loser'
                    score_value1 = 0
                    score_value2 = 0
                    player1x_change = 0
                    player1y_change = 0
                    player2x_change = 0
                    player2y_change = 0
                    obstacle21X = random.randint(70, 830)
                    obstacle31X = random.randint(70, 830)
                    laser1x_change = 0.6
                    laser3x_change = 0.7
                    laser2x_change = 0.8
                    laser4x_change = 0.9
                    laser5x_change = 0.5
                    laser11X = random.randint(70, 900)
                    laser14X = random.randint(70, 900)
                    laser16X = random.randint(70, 900)
                    laser51X = random.randint(70, 900)
                    laser52X = random.randint(70, 900)
                    laser1pass1 = True
                    laser1pass2 = True
                    laser2pass1 = True
                    laser2pass2 = True
                    laser3pass1 = True
                    laser3pass2 = True
                    laser4pass1 = True
                    laser4pass2 = True
                    laser5pass1 = True
                    laser5pass2 = True
                    obstacle21pass1 = True
                    obstacle21pass2 = True
                    obstacle31pass1 = True
                    obstacle31pass2 = True
                    asteroidpass1 = True
                    asteroidpass2 = True

            show_exit_screens(200, 270)
            show_exit_screenq(200, 370)
            show_score(200, 470)
            show_final_winner(200, 570)

            clock.tick(10000)
            pygame.display.update()

    while exit_screen:
        screen.fill(other_bg_color)
        screen.blit(background2, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_screen = False
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit_screen = False
                    run = False

        # if pygame.event == pygame.KEYUP :
                if event.key == pygame.K_q:
                    exit_sreen = False
                    run = False

                if event.key == pygame.K_SPACE:
                    exit_screen = False
                    run = True
                    player1X = 280
                    player1Y = 700
                    player2X = 470
                    player2Y = 700
                    player1life = True
                    player2life = True
                    time_value = 40000
                    scoreuptaken = False
                    scoreupx = random.randint(70, 800)
                    scoreupy = random.randint(12, 700)
                    asteroidX = random.randint(300, 900)
                    asteroidY = random.randint(0, 300)
                    status1 = 'Loser'
                    status2 = 'Loser'
                    player1x_change = 0
                    player1y_change = 0
                    player2x_change = 0
                    player2y_change = 0
                    obstacle21X = random.randint(70, 830)
                    obstacle31X = random.randint(70, 830)
                    laser1x_change += 0.5
                    laser3x_change += 0.5
                    laser2x_change += 0.5
                    laser4x_change += 0.5
                    laser5x_change += 0.5
                    laser11X = random.randint(70, 900)
                    laser14X = random.randint(70, 900)
                    laser16X = random.randint(70, 900)
                    laser51X = random.randint(70, 900)
                    laser52X = random.randint(70, 900)
                    laser1pass1 = True
                    laser1pass2 = True
                    laser2pass1 = True
                    laser2pass2 = True
                    laser3pass1 = True
                    laser3pass2 = True
                    laser4pass1 = True
                    laser4pass2 = True
                    laser5pass1 = True
                    laser5pass2 = True
                    obstacle21pass1 = True
                    obstacle21pass2 = True
                    obstacle31pass1 = True
                    obstacle31pass2 = True
                    asteroidpass1 = True
                    asteroidpass2 = True

        if not player1life and player2life:
            show_death1(200, 170)

        if not player2life and player1life:
            show_death2(200, 170)

        if not player1life and not player2life:
            show_death3(200, 170)

        if player1life and player2life:
            show_death4(200, 170)

        show_next_level(200, 270)
        show_exit_screenq(200, 370)
        show_score(200, 470)
        clock.tick(10000)
        pygame.display.update()
# print(1000-(pygame.time.get_ticks())%1000)
    clock.tick(10000)
    pygame.display.update()
