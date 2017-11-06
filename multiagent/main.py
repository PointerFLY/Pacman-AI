import pacman
from pacman import *
import os
import sys

if __name__ == '__main__':
    TestCase = True

    if TestCase:
        params = '-q q3'
        sys.argv = params.split(' ')
        execfile('autograder.py')
    else:
        params = '-p MinimaxAgent -k 2 --frameTime 0 -f -l openClassic -a depth=2 -g DirectionalGhost'
        sys.argv = params.split(' ')
        execfile('pacman.py')

