from game_functions import *

# Main game loop and events
def game_level1(player_x, player_y, player_speed, walls, startTime):
    running = True
    while running:
        pygame.time.delay(100)
        screen.fill(BG)

        # draw Start and Finish lines
        screen.blit(checkLine_s, (0, 0))
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
                endTime = pygame.time.get_ticks()
                gameOver(False, str((endTime - startTime) / 1000))
                running = False

            if hasWon(player_x, player_y):
                endTime = pygame.time.get_ticks()
                gameOver(True, str((endTime - startTime) / 1000))
                running = False

        pygame.display.update()

    return running
