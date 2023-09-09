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
# bg = pygame.image.load("F:/Study Materials/Python/Game/res/graphics/surround.png")

#Loading music
# pygame.mixer.music.load("./res/music/gb_music.wav")

# Player initial position
player_x = 20
player_y = screen.get_height()//2
player_speed = 2

# Fonts
font = pygame.font.Font('freesansbold.ttf', 32)


# Methods
def positionWall(i):
    #position walls in alternate positons
    if(i*100 < screen.get_width()-150):
        if i % 2 == 0:
            screen.blit(wall_lg, (i*110, 0))
        else:
            screen.blit(wall_lg, (i*110, 50))

def gameOver():
    gameOverText = font.render('GAME OVER!!', True, WHITE)
    pygame.screen.blit(gameOverText, (150, 300))
    # overSoud = pygame.mixer.Sound('D:\Python Projects\game\musics\Game_Over.wav')
    # overSoud.play()


def player(x, y):
    pygame.screen.blit(player, (x, y))

def hasCollied(wallPosX, wallPosY, playerPosX, playerPosY):
    distance = sqrt(pow(wallPosX - playerPosX, 2) + pow(wallPosY - playerPosY, 2))
    if distance < 10:
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

    pygame.display.update()
