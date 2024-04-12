import pygame
import random
import math
from pygame import mixer
import io
# Initializar PyGame
pygame.init()

# Create display
display = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption('Space Invasion')
icon = pygame.image.load('ovni.png')
pygame.display.set_icon(icon)
background = pygame.image.load('background.jpg')

# add music

mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Player
img_player = pygame.image.load('spacecraft.png')
player_x = 368
player_y = 500
player_x_change = 0

# Enemy
img_enemy = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
amount_enemy = 10

for e in range(amount_enemy):
    img_enemy.append(pygame.image.load('enemy.png'))
    enemy_x.append(random.randint(0,736))
    enemy_y.append(random.randint(10,200))
    enemy_x_change.append(.3)
    enemy_y_change.append(50)

# Bullet
img_bullet = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 500
bullet_x_change = 0
bullet_y_change = 3
bullet_active = False

def bytes_font(font):
    with open(font,'rb') as f:
        ttf_bytes = f.read()
    return io.BytesIO(ttf_bytes)

score = 0
font_bytes = bytes_font('font_number.ttf')
font = pygame.font.Font(font_bytes,32)
text_x = 10
text_y = 10

def view_score(x, y):
    text = font.render(f' Score: {score}',True, (255,255,255))
    display.blit(text,(x,y))

font_bytes_final = bytes_font('font_number.ttf')
font_two = pygame.font.Font(font_bytes_final,60)

def final_text():
    my_final_font = font_two.render(f' GAME OVER',True, (255,255,255))
    display.blit(my_final_font,(220,230))

# Player Function
def player(x,y):
    display.blit(img_player,(x,y))

# Enemy Function
def enemy(x,y,ene):
    display.blit(img_enemy[ene],(x,y))

# Bullet Function
def shoot_bullet(x,y):
    global bullet_active
    bullet_active = True
    display.blit(img_bullet,(x + 16,y + 10))

def validate_collision(x_1,y_1,x_2,y_2):
    distance = math.sqrt(math.pow(x_2 - x_1,2) + math.pow(y_2 - y_1,2))
    if distance < 27:
        return True
    else:
        return False


# Loop game
execute = True
while execute :
    for event in pygame.event.get():
        # Event Close
        if event.type == pygame.QUIT:
            execute = False
        #  Event Press Key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -.6
            if event.key == pygame.K_RIGHT:
                player_x_change =  .6
            if event.key == pygame.K_SPACE:
                if not bullet_active:
                    bullet_x = player_x
                    shoot_bullet(bullet_x,bullet_y)
                    sound_bullet = mixer.Sound('disparo.mp3')
                    sound_bullet.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                player_x_change = 0



    # Backgroun Image
    # display.fill((133,201,112))
    display.blit(background,(0,0))

    # limit the player margin
    player_x += player_x_change

    if player_x <= 0:
        player_x = 0
    if player_x >= 736:
        player_x = 736

    # limit the player enemy
    for e in range(amount_enemy):

        if enemy_y[e] > 430:
            for k in range(amount_enemy):
                enemy_y[k] = 1000
            final_text()
            break

        enemy_x[e] += enemy_x_change[e]

        if enemy_x[e] <= 0:
            enemy_x_change[e] = .3
            enemy_y[e] += enemy_y_change[e]
        if enemy_x[e] >= 736:
            enemy_x_change[e] = -.3
            enemy_y[e] += enemy_y_change[e]

    # Collision
        collision = validate_collision(enemy_x[e], enemy_y[e], bullet_x, bullet_y)
        if collision:
            sound_collision = mixer.Sound('Golpe.mp3')
            sound_collision.play()
            bullet_y = 500
            bullet_active = False
            score += 1
            enemy_x[e] = random.randint(0, 736)
            enemy_y[e] = random.randint(10, 200)
        enemy(enemy_x[e], enemy_y[e], e)

    # Move bullet
    if bullet_y <= -64:
        bullet_y = 500
        bullet_active = False
    if bullet_active:
        shoot_bullet(bullet_x,bullet_y)
        bullet_y -= bullet_y_change


    player(player_x, player_y)

    view_score(text_x,text_y)
    # Update Game
    pygame.display.update()