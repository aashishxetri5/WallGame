from game_functions import *


# Main game loop and events
def game_level1(player_x, player_y, player_speed, walls, startTime):
    running = True
    win = False
    while running:
        screen.fill(BG)

        # draw Start and Finish lines
        screen.blit(checkLine_s, (0, HEIGHT // 2), (0, HEIGHT // 2, 100, 100))
        screen.blit(checkLine_f, (screen.get_width() - 50, 0))

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

        player_x, player_y, running, win = mainControls(
            startTime, walls, 1, player_x, player_y, player_speed, running
        )

        pygame.display.update()

    return win


def rungame_1():
    startTime = pygame.time.get_ticks()
    status = game_level1(player_x, player_y, player_speed, walls_lvl1, startTime)
    pygame.time.delay(2000)
    return status  # returns true is the game level is complete
