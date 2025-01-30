import pygame
import random
import math
from pygame import mixer

# Initialize pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invasion")

# Load and set the game icon
icon = pygame.image.load("ovni.png")
pygame.display.set_icon(icon)

# Load background image
background = pygame.image.load("background.jpg")

# Load and play background music
mixer.music.load("MusicaFondo.mp3")
mixer.music.play(-1)

# Player settings
player_img = pygame.image.load("spaceship.png")
player_x = 368
player_y = 500
player_x_change = 0

# Score settings
score = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10

game_over_font = pygame.font.Font('freesansbold.ttf', 40)

# Enemy settings
enemy_img = pygame.image.load("enemy.png")
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50, 200)
enemy_x_change = 0.1  # Movement speed on the X-axis
enemy_y_change = 50    # Movement step on the Y-axis

# Bullet settings
bullet_img = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 500
bullet_y_change = 1  # Bullet speed
bullet_visible = False

# Function to draw the player at the given coordinates
def set_player(x, y):
    screen.blit(player_img, (x, y))

# Function to draw the enemy at the given coordinates
def set_enemy(x, y):
    screen.blit(enemy_img, (x, y))

# Function to shoot a bullet from the player
def shoot_bullet(x, y):
    global bullet_visible
    bullet_visible = True
    screen.blit(bullet_img, (x + 16, y))

# Function to check collision between bullet and enemy
def is_collision(x_1, x_2, y_1, y_2):
    distance = math.sqrt(math.pow((x_2 - x_1), 2) + math.pow((y_2 - y_1), 2))
    return distance < 36

# Function to display the score on the screen
def show_score(x, y):
    text = score_font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (x, y))

# Function to display the game over text
def game_over_text():
    text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(text, (280, 200))

# Main game loop
is_running = True
while is_running:
    # Set background image
    screen.blit(background, (0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        # Key press events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.2  # Move left
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.2   # Move right
            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound("disparo.mp3")
                bullet_sound.play()
                if not bullet_visible:
                    bullet_x = player_x
                    shoot_bullet(bullet_x, bullet_y)

        # Key release event
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player_x_change = 0

    # Update player position
    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Check for game over condition
    if enemy_y > 250:
        enemy_y = 1000  # Move enemy out of screen
        game_over_text()

    # Update enemy position
    enemy_x += enemy_x_change
    if enemy_x <= 0:
        enemy_x_change = 0.1
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -0.1
        enemy_y += enemy_y_change

    # Bullet movement
    if bullet_y <= -32:
        bullet_y = 500
        bullet_visible = False

    if bullet_visible:
        shoot_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # Collision detection
    collision = is_collision(enemy_x, bullet_x, enemy_y, bullet_y)
    if collision:
        collision_sound = mixer.Sound("Golpe.mp3")
        collision_sound.play()
        bullet_y = 500
        bullet_visible = False
        score += 1
        enemy_x = random.randint(0, 736)
        enemy_y = random.randint(50, 200)

    # Draw elements on screen
    set_player(player_x, player_y)
    set_enemy(enemy_x, enemy_y)
    show_score(text_x, text_y)

    # Update display
    pygame.display.update()
