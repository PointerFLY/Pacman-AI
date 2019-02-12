import sys

if __name__ == '__main__':
    isGrading = False

    if isGrading:
        params = 'autograder.py'
        sys.argv = params.split(' ')
        execfile('autograder.py')
    else:
        params = 'autograder.py -q q1'
        sys.argv = params.split(' ')
        execfile('autograder.py')
