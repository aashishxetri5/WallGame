import pygame, sys

pygame.init()

# Constants
WIDTH, HEIGHT = 900, 350
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG = (93, 255, 114)

file_log = open("logs.txt", "w")

# Track Score
score = 100

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
# pygame.mixer.Sound("F:/Study Materials/Python/WallGame/res/music/song.wav").play(-1)

# Player initial position
player_x = 20
player_y = screen.get_height() // 2
player_speed = 2


# Fonts
font = pygame.font.Font("freesansbold.ttf", 35)

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


# display score
def displayStat(score, level):
    score_f = level_f = pygame.font.Font("freesansbold.ttf", 18)

    score_text = score_f.render(f"Score: {score}", True, WHITE)
    level_text = score_f.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))


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
def gameOver(result, time, level):
    # Get center position of screen
    x_pos = screen.get_width() // 2
    y_pos = screen.get_height() // 2

    score = calculateScore(time, 15.0 if level == 1 else 18.0)

    text = ""
    if result:
        text = font.render(f"You Won!! Score: {score}", True, BLACK)
    else:
        score = 0
        text = font.render("GAME OVER!! Score: 0", True, BLACK)
        collision.set_volume(.7)
        collision.play()

    text_rect = text.get_rect(center=(x_pos, y_pos))
    screen.blit(text, text_rect)
    writeScore(score, time, level)


# Check if player has won
def hasWon(player_x, player_y):
    if player_x >= screen.get_width() - 70:
        return True
    else:
        return False


# Calculates score based on time taken
def calculateScore(time, FS_time):
    if float(time) <= FS_time:
        return 100
    elif float(time) >= 100.0:
        return 0
    else:
        score = round(100 - (abs(float(time)) - FS_time) * 2, 2)
        return score if score > 0.0 else 0.0


def writeScore(score, time, level):
    file_log.write(f"\nOn level {level}:\nScore: {score}\nTime: {time}")


def mainControls(startTime, walls, level, player_x, player_y, player_speed, running):
    # Check for key press
    win = False
    key = pygame.key.get_pressed()
    # Move player according to key pressed
    if key[pygame.K_RIGHT] and player_x < screen.get_width() - 10:  # Move right
        player_x += player_speed**1.25
    elif key[pygame.K_UP] and player_y > 0:  # Move up
        player_y -= player_speed
    elif key[pygame.K_DOWN] and player_y < screen.get_height() - 35:  # Move down
        player_y += player_speed

    endTime = pygame.time.get_ticks()
    time = (endTime - startTime) / 1000
    displayStat(calculateScore(time, 35.0), level)

    # check collision
    for wall in walls:
        if hasCollied(wall[0], wall[1], player_x, player_y):
            print("collide")
            endTime = pygame.time.get_ticks()
            gameOver(False, str((endTime - startTime) / 1000), level)
            running = False
            break

        if hasWon(player_x, player_y):
            print("won")
            endTime = pygame.time.get_ticks()
            gameOver(True, str((endTime - startTime) / 1000), level)
            running = False
            win = True
            break

    return player_x, player_y, running, win