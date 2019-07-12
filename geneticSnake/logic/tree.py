import random

class Node:
    def __init__(self, depth, maxDepth, bare = 0):
        self.depth = depth
        self.max = maxDepth
        self.type = random.randrange(0, 12)
        if depth == maxDepth:
            self.type = random.randrange(12, 16)
        self.children = []
        if bare:
            self.bareChildren()
    def bareChildren(self):
        # print(self.depth)
        # input()
        if self.depth < self.max:
            self.children.append(Node(self.depth+1,self.max,1))
            self.children.append(Node(self.depth+1,self.max,1))

    def getChild(self,position):
        if position >= len(self.children):
            print("index:", position ,"out of bounds brah, returning default \"0\" ")
            input()
            return self
        return self.children[position]


    def evaluate(self,arr):
        if self.type > 11:
            return self.type - 12
        if arr[self.type]:
            return 1
        else:
            return 0

    def mutate(self):
        r = random.randrange(0, self.max)
        node = self
        for i in range(0, r):
            randA = random.randrange(0, len(node.children))
            newNode =  node.children[randA]
            node = newNode
        if node.type > 11:
            node.type = random.randrange(12,16)
        else:
            node.type = random.randrange(0,11)


class Tree:
    def __init__(self, maxDepth):
        self.max = maxDepth
        self.firstParents = Node(0,maxDepth)
    def initTree(self):
        self.firstParents.bareChildren()

    def decideMove(self,arr):
        pos = 0
        node = self.firstParents
        for i in range(0,self.max):
            pos = node.evaluate(arr)
            # if i < self.max:
            node = node.getChild(pos)
        pos = node.evaluate(arr)
        return pos
        # r = random.randrange(0,1000)
        # if r < 3:
        #     print(arr)
        #     print(pos)
        #     input()




        # for i in range(4, 8):
        #     if args[i]:
        #         if args[i + 4]:
        #             if args[res[i]]:
        #                 return res[(i + 2) % 4]
        #             return res[i]
        #         return res[i - 4]

    # # wall
    # def ifWallUp(self,input,res):
    #     if input[0]:
    #         return 0
    #     else:
    #         return 1
    # def ifWallRight(self,input,res):
    #     if input[1]:
    #         return 0
    #     else:
    #         return 1
    # def ifWallDown(self,input,res):
    #     if input[2]:
    #         return 0
    #     else:
    #         return 1
    # def ifWallLeft(self,input,res):
    #     if input[3]:
    #         return 0
    #     else:
    #         return 1
    # # food
    # def ifFoodUp(self,input,res):
    #     if input[4]:
    #         return 0
    #     else:
    #         return 1
    # def ifFoodRight(self,input,res):
    #     if input[5]:
    #         return 0
    #     else:
    #         return 1
    # def ifFoodDown(self,input,res):
    #     if input[6]:
    #         return 0
    #     else:
    #         return 1
    # def ifFoodLeft(self,input,res):
    #     if input[7]:
    #         return 0
    #     else:
    #         return 1
    # # snake
    # def ifSnakeUp(self,input,res):
    #     if input[8]:
    #         return 0
    #     else:
    #         return 1
    # def ifSnakeRight(self,input,res):
    #     if input[9]:
    #         return 0
    #     else:
    #         return 1
    # def ifSnakeDown(self,input,res):
    #     if input[10]:
    #         return 0
    #     else:
    #         return 1
    # def ifSnakeLeft(self,input,res):
    #     if input[11]:
    #         return 0
    #     else:
    #         return 1
    # def evalAND(self,in1,in2,out1):
    #     if in1 and in2:
    #         return out1
    #
    # def evalAND(self, in1, in2, out1):
    #     if in1 and in2:
    #         return out1
