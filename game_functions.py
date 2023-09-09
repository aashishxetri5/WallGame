import pygame, sys

pygame.init()

# Constants
WIDTH, HEIGHT = 900, 350
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG = (93, 255, 114)
global endTime
# Track Score
score = 0

# Setting up screen and caption
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wall Game")

# Loading images
wall_lg = pygame.image.load(
    "F:/Study Materials/Python/WallGame/res/graphics/wall_lg.png"
)
playerCh = pygame.image.load(
    "F:/Study Materials/Python/WallGame/res/graphics/player.png"
)
checkLine_s = checkLine_f = pygame.image.load(
    "F:/Study Materials/Python/WallGame/res/graphics/checkLine.png"
)

# Loading Music
collision = pygame.mixer.Sound(
    "F:/Study Materials/Python/WallGame/res/music/killed.wav"
)
pygame.mixer.Sound("F:/Study Materials/Python/WallGame/res/music/song.wav").play(-1)

# Player initial position
player_x = 20
player_y = screen.get_height() // 2
player_speed = 10


# Fonts
font = pygame.font.Font("freesansbold.ttf", 32)

# wall position
walls_lvl1 = []


# Methods
# Position of walls
def positionWall(i):
    x = y = 0
    if i * 100 < screen.get_width() - 150:
        if i % 2 == 0:
            x = i * 140
            y = 0
        else:
            x = i * 140
            y = 50

        screen.blit(wall_lg, (x, y))
        walls_lvl1.append((x, y))


# Position of player
def player(x, y):
    screen.blit(playerCh, (x, y))


# Check collision between player and wall
def hasCollied(wallPosX, wallPosY, playerPosX, playerPosY):
    # Get width and height of player and wall
    wall_width = wall_lg.get_width()
    wall_height = wall_lg.get_height()
    player_width = playerCh.get_width()
    player_height = playerCh.get_height()

    # Create rectangles for player and wall
    player_rect = pygame.Rect(playerPosX, playerPosY, player_width, player_height)
    wall_rect = pygame.Rect(wallPosX, wallPosY, wall_width, wall_height)

    # Check if player and wall collide, return True if they do else False
    if player_rect.colliderect(wall_rect):
        return True
    else:
        return False


# Game over text
def gameOver(result, time):
    # Get center position of screen
    x_pos = screen.get_width() // 2
    y_pos = screen.get_height() // 2

    score = calculateScore(time)

    text = ""
    if result:
        text = font.render(f"YOU WON!! Score: {score}", True, BLACK)
    else:
        score = 0
        text = font.render("GAME OVER!! Score: 0", True, BLACK)
        collision.set_volume(1)
        collision.play()

    text_rect = text.get_rect(center=(x_pos, y_pos))
    screen.blit(text, text_rect)
    writeScore(score, time)


# Check if player has won
def hasWon(player_x, player_y):
    player_width = playerCh.get_width()
    player_height = playerCh.get_height()

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    finish_rect = pygame.Rect(screen.get_width() - 50, 0, 50, 50)

    if player_rect.colliderect(finish_rect):
        return True
    else:
        return False


def calculateScore(time):
    if time <= "20":
        return 100
    elif time >= "50":
        return 0
    else:
        return 100 - (float(time) - 20) * 2


def writeScore(score, time):
    file_log = open("logs.txt", "w")
    file_log.write(f"Score: {score}\nTime: {time}")
    file_log.close()
