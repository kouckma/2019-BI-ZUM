from logic import individual
from logic import tree
import random
import copy

def printTree(node,genomLen):
    arr = [[]]
    for i in range(0,genomLen):
        ar = []
        arr.append(ar)
    fillArr(node,arr)
    for x in arr:
        print(x)

def fillArr(node,arr):
    arr[node.depth].append(node.type)
    for x in node.children:
        fillArr(x,arr)


def crossTwo(par1, par2, genomLength,crossoverProbability):
    randArr = []
    for i in range(0, 3):
        # (genomLength - 1) perhaps ?
        randArr.append(random.randrange(1,genomLength))
    # print("pred:" ,randArr)
    # randArr.sort()
    # print("po:", randArr)
    # input()
    treeA = copy.deepcopy(par1.fTree)
    treeB = copy.deepcopy(par2.fTree)

    nodeParentA = None
    nodeParentB = None
    childA = treeA.firstParents
    childB = treeB.firstParents

    # print("behold")
    # printTree(treeA.firstParents,genomLength)
    # print("-------------")
    # printTree(treeB.firstParents,genomLength)
    # print("\ndidunow")
    # input()


    randA = 0
    randB = 0

    if crossoverProbability > random.random():
        for i in range(0, randArr[0]):
            nodeParentA = childA
            randA = random.randrange(0, len(nodeParentA.children))
            childA = nodeParentA.children[randA]
        for i in range(0, randArr[0]):
            nodeParentB = childB
            randB = random.randrange(0, len(nodeParentB.children))
            childB = nodeParentB.children[random.randrange(0, len(nodeParentB.children))]
        if randArr[0] != 0:
            # print("swapuju na depth:", randArr[0])
            # input()
            nodeParentA.children[randA] = childB
            nodeParentB.children[randB] = childA
    # else:
    #     print("neswapnul sem :(")

    # print("andNowBehold")
    # printTree(treeA.firstParents,genomLength)
    # print("-------------")
    # printTree(treeB.firstParents,genomLength)
    # print("\nDidUNow?")
    # input()

    # genomeA = []
    # genomeB = []
    # for i in range(0, randArr[0]):
    #     genomeA.append(par1.result[i])
    #     genomeB.append(par2.result[i])
    # for i in range(randArr[0], genomLength):
    #     genomeA.append(par2.result[i])
    #     genomeB.append(par1.result[i])

    # for i in range(0,randArr[0]):
    #     genomeA.append(par1.result[i])
    #     genomeB.append(par2.result[i])
    # for i in range(randArr[0],randArr[1]):
    #     genomeA.append(par2.result[i])
    #     genomeB.append(par1.result[i])
    # for i in range(randArr[1],randArr[2]):
    #     genomeA.append(par1.result[i])
    #     genomeB.append(par2.result[i])
    # for i in range(randArr[2],genomLength):
    #     genomeA.append(par2.result[i])
    #     genomeB.append(par1.result[i])

    a = individual.Snake(par1.width, par1.height, par1.turns, par1.startingPos, genomLength)
    a.fTree = treeA
    b = individual.Snake(par1.width, par1.height, par1.turns, par1.startingPos, genomLength)
    b.fTree = treeB
    return a, b


def crossoverPopulation(parents, genomLength,crossoverProbability = 0.05):
    tmp = parents[0]
    tmp2 = parents[0]
    children = []
    for i in range(0, len(parents)):
        if i % 2 == 0:
            tmp = parents[i]
        else:
            # if crossoverProbability > random.random():
            tmp2 = parents[i]
            a, b = crossTwo(tmp, tmp2, genomLength,crossoverProbability)
            children.append(a)
            children.append(b)

    return children


def mutatePopulation(embryos, mutations, mutationRate):
    # numberOfMutants = random.randrange(0,len(embryos)/4)
    # numberOfMutants = random.randrange(0,len(embryos))
    for x in range(0, len(embryos)):
        ran = random.random()
        if (ran < mutationRate):
            embryos[random.randrange(0, len(embryos))].mutate(mutations)
        #     print("mutuji")
        # print(ran)
        # input()
    return embryos


def getSurvivors(currentPop, heuristics, limit):
    survivors = []
    test = []
    for i in range(0, limit):
        bestHeur = -999999
        bestID = 0
        for j in range(0, int(len(currentPop) / 4)):
            adept = heuristics[random.randrange(0, len(currentPop))]
            if adept[0] > bestHeur:
                bestHeur = adept[0]
                bestID = adept[1]
        survivors.append(currentPop[bestID])
        test.append(bestID)
    return survivors, test
