import sys

if __name__ == '__main__':
    isGrading = not True

    if isGrading:
        params = 'autograder.py'
        sys.argv = params.split(' ')
        execfile('autograder.py')
    else:
        params = 'python autograder.py -q q1'
        sys.argv = params.split(' ')
        execfile('autograder.py')