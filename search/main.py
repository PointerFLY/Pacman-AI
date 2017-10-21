import pacman
from pacman import readCommand, runGames

argvStrList = []
for _ in range(20):
    argvStrList.append("")
argvStrList[0] = "-l mediumMaze -p SearchAgent --frameTime 0 -a fn=dfs"
argvStrList[1] = "-l mediumMaze -p SearchAgent --frameTime 0 -a fn=bfs"
argvStrList[2] = "-l mediumMaze -p SearchAgent --frameTime 0 -a fn=ucs"
argvStrList[3] = "-l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic"
argvStrList[4] = "-l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem --frameTime 0"
argvStrList[5] = "-l mediumCorners -p SearchAgent -a fn=aStarSearch,prob=CornersProblem,heuristic=cornersHeuristic -z 0.5 --frameTime 0"
argvStrList[6] = "-l trickySearch -p SearchAgent -a fn=astar,prob=FoodSearchProblem,heuristic=foodHeuristic --frameTime 0"
argvStrList[7] = "-l bigSearch -p ClosestDotSearchAgent -z 0.5 --frameTime 0"

for idx, argvStr in enumerate(argvStrList):
    if idx > 3:
        break
    print "********", idx, "*********"
    argvList = argvStr.split(" ")
    args = readCommand(argvList)
    runGames(**args)

# argvList = argvStrList[4].split(" ")
# args = readCommand(argvList)  # Get game components based on input
# runGames(**args)