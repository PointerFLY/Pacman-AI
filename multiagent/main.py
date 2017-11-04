import pacman
from pacman import *

if __name__ == '__main__':

    params = '-p ReflexAgent -k 2 -l openClassic --frameTime 0.1 -g RandomGhost'
    argv = params.split(' ')
    args = readCommand(argv)  # Get game components based on input
    runGames(**args)