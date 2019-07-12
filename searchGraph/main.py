import re
import os
import time
import collections
from sortedcontainers import SortedSet

clear = lambda: os.system('clear')
maxX = 0
maxY = 0
currentLine = ""
defaultArr = [[]]
parentArr = [[]]
costs = [[]]
tileCosts = [[]]

class Position:
    def __init__(self,INy = 0,INx = 0, prevY = 0, prevX = 0):
        self.posX = INx
        self.posY = INy
        self.posPrevX = prevX
        self.posPrevY = prevY
    def changeParent(self, y, x):
        self.posPrevX = x
        self.posPrevY = y


class Node:
    def __init__(self,INposition,INdepth ,INheur , INcost = 0):
        # print("y:", INposition.posY , "x:", INposition.posX)
        # print("Incost:",INcost)
        # input()
        self.cost = INcost
        self.pos = Position(0,0,0,0)
        self.pos.posX = INposition.posX
        self.pos.posY = INposition.posY
        self.pos.posPrevX = INposition.posPrevX
        self.pos.posPrevY = INposition.posPrevY
        self.depth = INdepth
        self.heur = INheur
    def changeParent(self, y, x):
        self.pos.posPrevX = x
        self.pos.posPrevY = y

def show (start,end,delay):
    clear()
    for i in range(maxY):
        for q in range(maxX):
            if (i == start.posY and q == start.posX):
                print('\033[1m'+'\033[32m'+"S"+'\033[0m', end="")
            elif (i == end.posY and q == end.posX):
                print('\033[1m'+'\033[31m'+"E"+'\033[0m', end="")
            else:
                if (defaultArr[i][q] == 0):
                    print(" ", end="")
                elif (defaultArr[i][q] == 1):
                    print('\033[m'+"X"+'\033[0m', end="")
                elif (defaultArr[i][q] == 2):
                    print('\033[1m'+"#"+'\033[0m', end="")
                elif (defaultArr[i][q] == 4):
                    print('\033[93m'+'\033[1m'+"*"+'\033[0m', end="")
                elif (defaultArr[i][q] == 5):
                    print("%", end="")
        print("")
    time.sleep(delay)

def showExpandedNodes(expanded):
    print("Nodes expaned:", expanded)

def showPath(expanded):
    cx = end.posX
    cy = end.posY
    n = 0
    while (1):
        tmpx = cx
        cx = parentArr[cy][tmpx].posPrevX
        cy = parentArr[cy][tmpx].posPrevY
        if cx == start.posX and cy == start.posY:
            break
        if cx < 0 or cy < 0:
            break
        n += 1
        defaultArr[cy][cx] = 4

        show(start, end, 0.2)
        print("----------------------------------------------")
        showExpandedNodes(expanded)
        print("Path length:",n)

def random(expanded):
    queue = set()
    queue.add(start)

    while (queue):
        currentNode = queue.pop()
        if currentNode.posY == end.posY and currentNode.posX == end.posX:
            break
        x = currentNode.posX
        y = currentNode.posY
        if y < maxY and defaultArr[y + 1][x] == 0:
            expanded += 1
            defaultArr[y+1][x] = 2
            pos = Position(y + 1, x, y, x)
            queue.add(pos)
            parentArr[y + 1][x].changeParent(y, x)
        if y > 0 and defaultArr[y - 1][x] == 0:
            expanded += 1
            defaultArr[y-1][x] = 2
            pos = Position(y - 1, x, y, x)
            queue.add(pos)
            parentArr[y - 1][x].changeParent(y, x)
        if x < maxX and defaultArr[y][x + 1] == 0:
            expanded += 1
            defaultArr[y][x+1] = 2
            pos = Position(y, x + 1, y, x)
            queue.add(pos)
            parentArr[y][x + 1].changeParent(y, x)
        if x > 0 and defaultArr[y][x - 1] == 0:
            expanded += 1
            defaultArr[y][x-1] = 2
            pos = Position(y, x - 1, y, x)
            queue.add(pos)
            parentArr[y][x - 1].changeParent(y, x)
        defaultArr[y][x] = 2

        show(start, end,0.01)

    showPath(expanded)


def dfs (expanded):
    qu = collections.deque()
    qu.appendleft(start)

    while (qu):
        # currentLine = input()
        currentNode = qu.popleft()
        if currentNode.posY == end.posY and currentNode.posX == end.posX:
            break
        x = currentNode.posX
        y = currentNode.posY
        if y < maxY and defaultArr[y + 1][x] == 0:
            expanded += 1
            defaultArr[y+1][x] = 2
            pos = Position(y + 1, x, y, x)
            qu.appendleft(pos)
            parentArr[y + 1][x].changeParent(y, x)
        elif y > 0 and defaultArr[y - 1][x] == 0:
            expanded += 1
            defaultArr[y-1][x] = 2
            pos = Position(y - 1, x, y, x)
            qu.appendleft(pos)
            parentArr[y - 1][x].changeParent(y, x)
        elif x < maxX and defaultArr[y][x + 1] == 0:
            expanded += 1
            defaultArr[y][x+1] = 2
            pos = Position(y, x + 1, y, x)
            qu.appendleft(pos)
            parentArr[y][x + 1].changeParent(y, x)
        elif x > 0 and defaultArr[y][x - 1] == 0:
            expanded += 1
            defaultArr[y][x-1] = 2
            pos = Position(y, x - 1, y, x)
            qu.appendleft(pos)
            parentArr[y][x - 1].changeParent(y, x)
        defaultArr[y][x] = 2

        show(start, end, 0.01)
    showPath(expanded)


def betterBfs (expanded):
    # queue = [start]
    qu = collections.deque()
    qu.append(start)

    while (qu):
        currentNode = qu.popleft()
        if currentNode.posY == end.posY and currentNode.posX == end.posX:
            break
        x = currentNode.posX
        y = currentNode.posY
        if y < maxY and defaultArr[y + 1][x] == 0:
            expanded += 1
            pos = Position(y + 1, x, y, x)
            qu.append(pos)
            parentArr[y + 1][x].changeParent(y, x)
            defaultArr[y+1][x] = 2
        if y > 0 and defaultArr[y - 1][x] == 0:
            expanded += 1
            pos = Position(y - 1, x, y, x)
            qu.append(pos)
            parentArr[y - 1][x].changeParent(y, x)
            defaultArr[y-1][x] = 2
        if x < maxX and defaultArr[y][x + 1] == 0:
            expanded += 1
            pos = Position(y, x + 1, y, x)
            qu.append(pos)
            parentArr[y][x + 1].changeParent(y, x)
            defaultArr[y][x+1] = 2
        if x > 0 and defaultArr[y][x - 1] == 0:
            expanded += 1
            pos = Position(y, x - 1, y, x)
            qu.append(pos)
            parentArr[y][x - 1].changeParent(y, x)
            defaultArr[y][x-1] = 2
        defaultArr[y][x] = 2

        show(start, end, 0.01)
    showPath(expanded)

def heuristic(depth,pos):
    return depth + abs(pos.posX - end.posX) + abs(pos.posY - end.posY)

def basicHeuristic(depth,pos):
    return abs(pos.posX - end.posX) + abs(pos.posY - end.posY)


def sortByDepth(nod):
    return nod.depth

def sortByHeur(nod):
    return nod.heur

def getIncost(y,x):
    return tileCosts[y][x]

def greedyNode(y,x,pary,parx,currDepth,qu):
    if (defaultArr[y][x] == 0 or defaultArr[y][x] == 5):
        defaultArr[y][x] = 2
        pos = Position(y, x, pary, parx)
        newNode = Node(pos, currDepth + 1, basicHeuristic(currDepth + 1, pos))
        qu.add(newNode)
        parentArr[y][x].changeParent(pary, parx)
        return 1
    return 0

def dijkstraNode(y,x,parentY,parentX,currDepth,cost,qu):
    if (defaultArr[y][x] == 0 or defaultArr[y][x] == 5) or (defaultArr[y][x] == 2 and costs[y][x] > currDepth + cost):
        incost = getIncost(y, x)
        defaultArr[y][x] = 2
        pos = Position(y, x, parentY, parentX)
        newNode = Node(pos, currDepth + cost, heuristic(currDepth + cost, pos), incost)
        costs[y][x] = currDepth + cost
        qu.add(newNode)
        parentArr[y][x].changeParent(parentY, parentX)
        return 1
    return 0

def greedy(expanded):
    startNode = Node(start,0,basicHeuristic(0,start))
    qu = SortedSet([startNode],sortByHeur)

    while (qu):
        currentNode = qu.pop(0)
        currDepth = currentNode.depth
        currHeur = currentNode.heur
        x = currentNode.pos.posX
        y = currentNode.pos.posY
        if y == end.posY and x == end.posX:
            break

        expanded += greedyNode(y + 1, x, y, x, currDepth, qu)
        expanded += greedyNode(y - 1, x, y, x, currDepth, qu)
        expanded += greedyNode(y, x + 1, y, x, currDepth, qu)
        expanded += greedyNode(y, x - 1, y, x, currDepth, qu)


        defaultArr[y][x] = 2

        show(start, end, 0.01)

    showPath(expanded)



def dijkstra(expanded):
    startNode = Node(start,0,heuristic(0,start))
    qu = SortedSet([startNode],sortByDepth)
    while (qu):
        currentNode = qu.pop(0)
        currDepth = currentNode.depth
        currHeur = currentNode.heur
        x = currentNode.pos.posX
        y = currentNode.pos.posY
        cost = currentNode.cost
        if y == end.posY and x == end.posX:
            break

        # needed when without borders
        # if y > 0 ; y < max .... etc
        tmpexpanded = expanded
        expanded += dijkstraNode(y+1,x,y,x,currDepth,cost,qu)
        expanded += dijkstraNode(y-1,x,y,x,currDepth,cost,qu)
        expanded += dijkstraNode(y,x+1,y,x,currDepth,cost,qu)
        expanded += dijkstraNode(y,x-1,y,x,currDepth,cost,qu)

        defaultArr[y][x] = 2

        show(start, end, 0.01)
    showPath(expanded)


def itsTheSame():
    show(start, end, 0.1)
    print("S == E")
    print("Nodes expaned:", 0)
    print("Path length:", 0)

def AstartNode(y,x,parentY,parentX,currDepth,qu):
    if (defaultArr[y][x] == 0):
        defaultArr[y][x] = 2
        pos = Position(y, x, parentY, parentX)
        newNode = Node(pos, currDepth + 1, heuristic(currDepth + 1, pos))
        qu.add(newNode)
        parentArr[y][x].changeParent(parentY, parentX)
        return 1
    return 0

def Astar(expanded):
    startNode = Node(start,0,heuristic(0,start))
    qu = SortedSet([startNode],sortByHeur)

    while (qu):
        currentNode = qu.pop(0)
        currDepth = currentNode.depth
        currHeur = currentNode.heur
        x = currentNode.pos.posX
        y = currentNode.pos.posY
        if y == end.posY and x == end.posX:
            break
        expanded += AstartNode(y+1,x,y,x,currDepth,qu)
        expanded += AstartNode(y-1,x,y,x,currDepth,qu)
        expanded += AstartNode(y,x+1,y,x,currDepth,qu)
        expanded += AstartNode(y,x-1,y,x,currDepth,qu)
        defaultArr[y][x] = 2

        show(start, end, 0.01)

    showPath(expanded)



# =====================================================================================
# reading of input
while (1):
    currentLine = input()
    if (currentLine.startswith("start") or currentLine.startswith("end")):
        break
    else:
        col = []
        for i in currentLine:
            if (i == "X"):
                col.append(1)
            elif (i == " "):
                col.append(0)
            elif (i == "%"):
                col.append(5)
        defaultArr.insert(maxY, col)
        maxX = len(currentLine)
        maxY += 1
StartPosX = int(re.search(r'\d+', currentLine).group())
StartPosY = int(re.search('\d+$', currentLine).group())
start = Position(StartPosY,StartPosX,-1,-1)

currentLine = input()
EndPosX = int(re.search(r'\d+', currentLine).group())
EndPosY = int(re.search('\d+$', currentLine).group())
end = Position(EndPosY,EndPosX , -1,-1)

for i in range(maxY - 1):
    col = []
    for q in range(maxX):
        col.append(Position(i,q,-1,-1))
    parentArr.insert(i,col)

for i in range(maxY - 1):
    col = []
    for q in range(maxX):
        col.append(999)
    costs.insert(i,col)

for i in range(maxY - 1):
    col = []
    for q in range(maxX):
        if defaultArr[i][q] == 5:
            col.append(10)
        else:
            col.append(1)
    tileCosts.insert(i,col)

# ==========================================================================================
# algorithm

clear()


print("choose search algorithm to be used:")
print("random search - 1")
print("DFS - 2")
print("BFS - 3")
print("dijkstra - 4")
print("Astar - 5")
print("greedyBFS - 6")

expanded = 0

answ = input()

if(start.posX == end.posX and start.posY == end.posY):
    itsTheSame()
elif answ == "1":
    random(expanded)
elif answ == "2":
    dfs(expanded)
elif answ == "3":
    betterBfs(expanded)
elif answ == "4":
    dijkstra(expanded)
elif answ == "5":
    Astar(expanded)
elif answ == "6":
    greedy(expanded)