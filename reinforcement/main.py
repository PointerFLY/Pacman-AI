import sys

if __name__ == '__main__':
    TestCase = True

    if TestCase:
        params = 'gridwoard.py -a value -i 5'
        sys.argv = params.split(' ')
        execfile('gridworld.py')
    else:
        params = 'pacman.py -p MinimaxAgent -l openClassic -a depth=3 --frameTime 3'
        sys.argv = params.split(' ')
        execfile('pacman.py')