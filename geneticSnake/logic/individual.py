import random
import os
import time
from logic import space
from logic import tree
from collections import deque

clear = lambda: os.system('clear')
foodCost = 2500
obstacleCost = -500

def sortByHeur(snek):
    return snek.fitness


# directions
# 0 = up
# 1 = right
# 2 = down
# 3 = left

# objects in map
# 0 = empty
# 1 = snake
# 2 = wall
# 3 = food

class Snake:
    def __init__(self, width, height, turns, startingPosition, genomeLength, moves=None):
        self.map = self.initArray(width, height)
        self.startingPos = startingPosition
        # self.foodPosition = foodPosition
        self.maxDepth = genomeLength
        self.fTree = tree.Tree(self.maxDepth)
        self.fTree.initTree()
        # print(self.fTree.max)
        # input()
        self.width = width
        self.height = height
        self.turns = turns
        self.genomeLength = genomeLength
        # self.argsCount = argsCount
        self.delay = 0.03
        self.foodPositions = []
        self.fitness = -1

    # param: y,x,arr, Lwall,Rwall,UWall,Dwall, Ufood...
    def moveFunction(self, y, x, args, visualize=0):
        decision = self.fTree.decideMove(args)
        # if visualize:
        #     print("decision:",decision)
        #     input()
        if decision > 3 or decision < 0:
            print("error invalid decision number (not 0,1,2,3)")
            input()
        return decision

    # functionInput = [
    # UPwall, 0
    # Rwall,
    # DOWNwall,
    # Lwall, 3

    # UPfood, 4
    # Rfood,
    # DOWNfood,
    # Lfood, 7

    # UPsnake, 8
    # Rsnake,
    # DOWNsnake,
    # Lsnake, 11
    # ]
    def getMoveFuncInput(self, arr, y, x, foodY, foodX, visualize=0):
        res = []
        if arr[y + 1][x] == 2:
            res.append(1)
        else:
            res.append(0)
        if arr[y][x + 1] == 2:
            res.append(1)
        else:
            res.append(0)
        if arr[y - 1][x] == 2:
            res.append(1)
        else:
            res.append(0)
        if arr[y][x - 1] == 2:
            res.append(1)
        else:
            res.append(0)
        #     food
        if foodY > y:
            res.append(1)
        else:
            res.append(0)
        if foodX > x:
            res.append(1)
        else:
            res.append(0)
        if foodY < y:
            res.append(1)
        else:
            res.append(0)
        if foodX < x:
            res.append(1)
        else:
            res.append(0)
        # snake
        if arr[y + 1][x] == 1:
            res.append(1)
        else:
            res.append(0)
        if arr[y][x + 1] == 1:
            res.append(1)
        else:
            res.append(0)
        if arr[y - 1][x] == 1:
            res.append(1)
        else:
            res.append(0)
        if arr[y][x - 1] == 1:
            res.append(1)
        else:
            res.append(0)

        return res

    def newFood(self, arr,visualize,foodCount):
        if visualize:
            foodY = self.foodPositions[foodCount][0]
            foodX = self.foodPositions[foodCount][1]
            arr[foodY][foodX] = 3
        else:
            h = self.height
            w = self.width
            foodY = 1
            foodX = 1
            done = 0
            while (done == 0):
                foodY = random.randrange(h)
                foodX = random.randrange(w)
                if arr[foodY][foodX] == 0:
                    arr[foodY][foodX] = 3
                    done = 1
            self.foodPositions.append([foodY,foodX])
            # print("appenduju",foodY,foodX)
        return foodY, foodX

    def simulate(self, visualize=0, id=0,aver = 0):
        self.map = self.initArray(self.width, self.height)
        if not visualize:
            self.foodPositions = []
        else:
            print(self.foodPositions)
            # input()
        y = self.startingPos[0]
        x = self.startingPos[1]
        arr = self.map
        body = []
        body.append([y, x])
        arr[y][x] = 1
        foodCount = 0
        foodY, foodX = self.newFood(arr,visualize,foodCount)
        if visualize:
            print(foodY,foodX)
            print(arr[foodY][foodX])
            # input()
        foodCount+=1

        heur = 0
        turn = 0

        for i in range(0, self.turns):
            turn += 1
            y = body[len(body) - 1][0]
            x = body[len(body) - 1][1]
            moveInput = self.getMoveFuncInput(arr, y, x, foodY, foodX, visualize)
            direction = self.moveFunction(y, x, moveInput, visualize)
            tmpheur = self.move(i, arr, body, moveInput, y, x, direction, visualize)
            if tmpheur == foodCost:
                foodY, foodX = self.newFood(arr,visualize,foodCount)
                foodCount+=1
            heur += tmpheur
            if visualize == 1:
                # clear()
                # for i in range(0, self.height):
                #     print(arr[i])
                space.show(arr, self.height, self.width, self.delay)
                print("heuristic:",heur)
                print("average:",aver)
                # print("snake head y,x:", y, x)
                # print("food y,x:", foodY, foodX)
                # print("direction == ", direction)
                print("turns:", turn, "out of", self.turns)
                # print(moveInput)
                print("generation:", id)
                time.sleep(self.delay)
        self.fitness = heur
        return heur

    def move(self, turn, arr, body, moveInput, y, x, direction, visualize=0):
        curry, currx = self.getCurrentXY(y, x, direction)

        tmpRes = self.evalPlace(arr, curry, currx, visualize)

        if tmpRes >= 0:
            if tmpRes == foodCost:
                body.append([curry, currx, -1])
                arr[curry][currx] = 1
            else:
                for i in range(0, len(body) - 1):
                    triple = body[i]
                    nextTriple = body[i + 1]
                    body[i] = [nextTriple[0], nextTriple[1]]
                    if i == 0:
                        arr[triple[0]][triple[1]] = 0
                        # print("1y, x:",triple[0],triple[1])
                body[len(body) - 1] = [curry, currx]
                arr[curry][currx] = 1
                if len(body) == 1:
                    arr[y][x] = 0
                # print("2y, x:", curry, currx)

        # if visualize == 1:
        #     input()
        # return tmpRes, arr
        return tmpRes

    def getCurrentXY(self, y, x, direction):
        curry = y
        currx = x
        if direction == 0:
            curry += 1
        elif direction == 1:
            currx += 1
        elif direction == 2:
            curry -= 1
        elif direction == 3:
            currx -= 1
        return curry, currx

    def evalPlace(self, arr, curry, currx, visualize=0):
        if arr[curry][currx] == 0:
            return 0
        elif arr[curry][currx] == 1:
            return obstacleCost
        elif arr[curry][currx] == 2:
            return obstacleCost
        elif arr[curry][currx] == 3:
            # if visualize:
            #     print("co ted")
            #     input()
            return foodCost
        return -1


    def mutate(self,mutations):

        for i in range(0,mutations):
            self.fTree.firstParents.mutate()

    def visualize(self, id,aver):
        self.simulate(1, id,aver)

    def initArray(self, width, height):
        arr = []
        tmpcol = []
        for i in range(0, width):
            tmpcol.append(2)
        arr.append(tmpcol)
        for i in range(1, height - 1):
            col = []
            col.append(2)
            for j in range(1, width - 1):
                col.append(0)
            col.append(2)
            arr.append(col)
        tmpcol = []
        for i in range(0, width):
            tmpcol.append(2)
        arr.append(tmpcol)

        # self.buildWall(arr,height,width)

        return arr

    def buildWall(self,arr,height,width):
        for i in range(int(height/4),int((height/4)*3)):
            arr[i][int(width/2)] = 2


    # def deepCopyI(self):
    #     Ires = []
    #     for i in range(0,len(self.result)):
    #         Ires.append(self.result[i])
    #     ind = Snake(self.width, self.height, self.turns, self.startingPos,self.genomeLength, Ires)
    #     return ind


    # def getRandRes(self):
    #     arr = []
    #     for i in range(0, self.genomeLength):
    #         arr.append(random.randrange(4))
    #     return arr