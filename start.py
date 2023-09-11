from wallGame_1 import rungame_1
from wallGame_2 import rungame_2
from game_functions import file_log
from pygame import quit
from sys import exit

level1 = rungame_1()
if level1 == True:
    rungame_2()

file_log.close()
quit()
exit()
