import pacman
from pacman import *
import os
import sys

if __name__ == '__main__':
    TestCase = True

    if TestCase:
        params = '--no-graphics'
        sys.argv = params.split(' ')
        execfile('autograder.py')
    else:
        params = 'pacman.py -p MinimaxAgent -l openClassic -a depth=3 --frameTime 3'
        sys.argv = params.split(' ')
        execfile('pacman.py')

