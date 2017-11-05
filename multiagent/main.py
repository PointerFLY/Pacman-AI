import pacman
from pacman import *

if __name__ == '__main__':

    params = '-p MinimaxAgent -k 1 --frameTime 1 -l mediumClassic -a depth=1'
    argv = params.split(' ')
    args = readCommand(argv)  # Get game components based on input
    runGames(**args)