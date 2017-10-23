import pacman
from pacman import readCommand, runGames
from autograder import *
import re
import os

argvStrList = []
for _ in range(20):
    argvStrList.append("")
argvStrList[0] = "-l mediumMaze -p SearchAgent -a fn=dfs --frameTime 0"
argvStrList[1] = "-l mediumMaze -p SearchAgent -a fn=bfs --frameTime 0"
argvStrList[2] = "-l mediumMaze -p SearchAgent -a fn=ucs --frameTime 0"
argvStrList[3] = "-l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic --frameTime 0"
argvStrList[4] = "-l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem --frameTime 0"
argvStrList[5] = "-l mediumCorners -p AStarCornersAgent -z 0.5 --frameTime 0"
argvStrList[6] = "-l trickySearch -p AStarFoodSearchAgent --frameTime 0"
argvStrList[7] = "-l bigSearch -p ClosestDotSearchAgent -z 0.5 --frameTime 0"

def test():
    argvList = "-q q3".split(" ")
    options = readCommand(argvList)
    if options.generateSolutions:
        confirmGenerate()
    codePaths = options.studentCode.split(',')

    moduleDict = {}
    for cp in codePaths:
        moduleName = re.match('.*?([^/]*)\.py', cp).group(1)
        moduleDict[moduleName] = loadModuleFile(moduleName, os.path.join(options.codeRoot, cp))
    moduleName = re.match('.*?([^/]*)\.py', options.testCaseCode).group(1)
    moduleDict['projectTestClasses'] = loadModuleFile(moduleName, os.path.join(options.codeRoot, options.testCaseCode))

    if options.runTest != None:
        runTest(options.runTest, moduleDict, printTestCase=options.printTestCase, display=getDisplay(True, options))
    else:
        evaluate(options.generateSolutions, options.testRoot, moduleDict,
                 gsOutput=options.gsOutput,
                 edxOutput=options.edxOutput, muteOutput=options.muteOutput, printTestCase=options.printTestCase,
                 questionToGrade=options.gradeQuestion, display=getDisplay(options.gradeQuestion != None, options))


def debug():
    for idx, argvStr in enumerate(argvStrList):
        start = 0
        if idx in range(0, 8):
            print "********", idx, "*********"
            argvList = argvStr.split(" ")
            args = pacman.readCommand(argvList)
            pacman.runGames(**args)

    # argvList = argvStrList[4].split(" ")
    # args = pacman.readCommand(argvList)  # Get game components based on input
    # pacman.runGames(**args)


debug()