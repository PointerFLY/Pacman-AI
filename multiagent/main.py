import pacman
from pacman import *

if __name__ == '__main__':

    params = '-p MinimaxAgent -k 1 --frameTime 0 -l mediumClassic -a depth=1 -g DirectionalGhost'
    argv = params.split(' ')
    args = readCommand(argv)  # Get game components based on input
    runGames(**args)