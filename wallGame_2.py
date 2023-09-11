from game_functions import *
from random import randint

walls_lvl2 = []
level = 2


# Position of walls
def positionWall2(i):
    x = y = 0
    if i * 100 < screen.get_width() - 150:
        angle = 0.0
        if i % 2 == 0:
            x = i * 130
            y = -10 + randint(0, 22)
        else:
            x = i * 130
            y = 80 + randint(0, 15)

        screen.blit(wall_lg, (x, y))
        walls_lvl2.append((x, y))


def game_level2(player_x, player_y, walls, startTime):
    running = True
    player_speed = 1.5
    while running:
        screen.fill(BG)

        # draw Start and Finish lines
        screen.blit(checkLine_s, (0, HEIGHT // 2), (0, HEIGHT // 2, 100, 100))
        screen.blit(checkLine_f, (screen.get_width() - 50, 0))

        # draw walls
        for i in range(1, 6):
            positionWall2(i)

        # draw player
        player(player_x, player_y)

        # Check if quit event is triggered
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player_x, player_y, running, win = mainControls(
            startTime, walls, 2, player_x, player_y, player_speed, running
        )

        pygame.display.update()


def rungame_2():
    startTime = pygame.time.get_ticks()
    game_level2(player_x, player_y, walls_lvl2, startTime)
    pygame.time.delay(2000)
