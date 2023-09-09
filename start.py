import pygame, sys

from wallGame_1 import *
from wallGame_2 import *

startTime = pygame.time.get_ticks()
status = game_level1(player_x, player_y, player_speed, walls_lvl1, startTime)

if status == False:
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()




