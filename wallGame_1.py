import pygame, sys

from math import sqrt, pow

file_log = open("logs.txt", "w")

pygame.init()

# Constants
WIDTH, HEIGHT = 900, 350
WHITE = (255, 255, 255)
BG = (93, 255, 114)

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

# Loading music
# pygame.mixer.music.load("./res/music/gb_music.wav")


# Player initial position
player_x = 20
player_y = screen.get_height() // 2
player_speed = 10


# Fonts
font = pygame.font.Font("freesansbold.ttf", 32)

# wall position
walls = []


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
        walls.append((x, y))


# Position of player
def player(x, y):
    screen.blit(playerCh, (x, y))


# Check collision between player and wall
def hasCollied(wallPosX, wallPosY, playerPosX, playerPosY):
    wall_width = wall_lg.get_width()
    wall_height = wall_lg.get_height()
    player_width = playerCh.get_width()
    player_height = playerCh.get_height()

    player_rect = pygame.Rect(playerPosX, playerPosY, player_width, player_height)
    wall_rect = pygame.Rect(wallPosX, wallPosY, wall_width, wall_height)

    if player_rect.colliderect(wall_rect):
        return True
    else:
        return False


# Game over text
def gameOver(result):
    x_pos = screen.get_width() // 2
    y_pos = screen.get_height() // 2
    if result:
        winText = font.render("YOU WON!!", True, WHITE)
        screen.blit(winText, (x_pos, y_pos))
    else:
        gameOverText = font.render("GAME OVER!!", True, WHITE)
        screen.blit(gameOverText, (x_pos, y_pos))
        # overSoud = pygame.mixer.Sound('D:\Python Projects\game\musics\Game_Over.wav')
        # overSoud.play()


# Check if player has won
def hasWon():
    if player_x >= screen.get_width() - 50:
        return True
    else:
        return False


# Main game loop and events
running = True
while running:
    pygame.time.delay(100)
    screen.fill(BG)

    # draw walls
    for i in range(1, 6):
        positionWall(i)

    # draw player
    player(player_x, player_y)

    # Check if quit event is triggered
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Check for key press
    key = pygame.key.get_pressed()

    # Move player according to key pressed
    if key[pygame.K_RIGHT] and player_x < screen.get_width() - 50:  # Move right
        player_x += player_speed
    elif key[pygame.K_UP] and player_y > 0:  # Move up
        player_y -= player_speed
    elif key[pygame.K_DOWN] and player_y < screen.get_height() - 50:  # Move down
        player_y += player_speed

    # check collision
    for wall in walls:
        if hasCollied(wall[0], wall[1], player_x, player_y):
            gameOver(False)
            running = False

        if hasWon():
            gameOver(True)
            running = False

        file_log.write(f"Player Position: {player_x}, {player_y}\n")
        file_log.write(f"Wall Position: {wall[0]}, {wall[1]}\n")

    pygame.display.update()

while(running == False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()