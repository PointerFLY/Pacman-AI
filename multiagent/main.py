import pacman
from pacman import *

if __name__ == '__main__':

    params = '-p MinimaxAgent -k 2 --frameTime 0 -l openClassic -a depth=2 -g DirectionalGhost'
    argv = params.split(' ')
    args = readCommand(argv)  # Get game components based on input
    runGames(**args)