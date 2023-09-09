import pygame, sys

from math import sqrt, pow

pygame.init()

# Constants
WIDTH, HEIGHT = 750, 350
WHITE = (255, 255, 255)
BG = (93,255,114)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Wall Game")

# Loading images

wall_lg = pygame.image.load("F:/Study Materials/Python/WallGame/res/graphics/wall_lg.png")
playerCh = pygame.image.load("F:/Study Materials/Python/WallGame/res/graphics/player.png")

#Loading music
# pygame.mixer.music.load("./res/music/gb_music.wav")

# Player initial position
player_x = 20
player_y = screen.get_height()//2
player_speed = 10

# Fonts
font = pygame.font.Font('freesansbold.ttf', 32)

# wall position
walls = []

# Methods
def positionWall(i):
    #position walls in alternate positons
    x = y = 0
    if(i*100 < screen.get_width()-150):
        if i % 2 == 0:
            x = i*100
            y = 0
        else:
            x = i*100
            y = 50

        screen.blit(wall_lg, (x, y))
        walls.append((x, y))

def gameOver():
    gameOverText = font.render('GAME OVER!!', True, WHITE)
    screen.blit(gameOverText, (150, 300))
    # overSoud = pygame.mixer.Sound('D:\Python Projects\game\musics\Game_Over.wav')
    # overSoud.play()


def player(x, y):
    screen.blit(playerCh, (x, y))

def hasCollied(wallPosX, wallPosY, playerPosX, playerPosY):
    distance = sqrt(pow(wallPosX - playerPosX, 2) + pow(wallPosY - playerPosY, 2))
    if distance < 50:
        return True
    else:
        return False


running = True
while running:
    pygame.time.delay(100)
    screen.fill(BG)

    #draw walls
    for i in range(1, 6):
        positionWall(i)

    #draw player
    player(player_x, player_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    elif key[pygame.K_RIGHT] and player_x < screen.get_width()-50:
        player_x += player_speed
    elif key[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    elif key[pygame.K_DOWN] and player_y < screen.get_height()-50:
        player_y += player_speed

    # check collision
    for wall in walls:
        if hasCollied(wall[0], wall[1], player_x, player_y):
            gameOver()
            running = False

    pygame.display.update()
