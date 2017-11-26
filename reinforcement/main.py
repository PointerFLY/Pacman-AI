import sys

if __name__ == '__main__':
    TestCase = True

    if TestCase:
        params = 'autograder.py'
        sys.argv = params.split(' ')
        execfile('autograder.py')
    else:
        params = 'pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumClassic'
        sys.argv = params.split(' ')
        execfile('pacman.py')