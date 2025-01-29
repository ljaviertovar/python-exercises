import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invasion")

icon = pygame.image.load("ovni.png")
pygame.display.set_icon(icon)
background = pygame.image.load("background.jpg")

player_img = pygame.image.load("spaceship.png")
player_x = 368
player_y = 500
player_x_change = 0

enemy_img = pygame.image.load("enemy.png")
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50, 200)
enemy_x_change = 0.1
enemy_y_change = 50

bullet_img = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 500
bullet_y_change = 1
bullet_visible = False


def set_player(x, y):
    screen.blit(player_img, (x, y))


def set_enemy(x, y):
    screen.blit(enemy_img, (x, y))


def shoot_bullet(x, y):
    global bullet_visible
    bullet_visible = True
    screen.blit(bullet_img, (x + 16, y ))


is_running = True
while is_running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.1
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.1
            if event.key == pygame.K_SPACE:
                if not bullet_visible:
                    bullet_x = player_x
                    shoot_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    enemy_x += enemy_x_change
    if enemy_x <= 0:
        enemy_x_change = 0.1
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -0.1
        enemy_y += enemy_y_change

    if bullet_y <= -32:
        bullet_y = 500
        bullet_visible = False

    if bullet_visible:
        shoot_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    set_player(player_x, player_y)
    set_enemy(enemy_x, enemy_y)

    pygame.display.update()
