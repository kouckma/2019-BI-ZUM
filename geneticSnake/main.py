from logic import individual
from logic import space
from logic import population
import os
import copy

width = 40
height = 40
popLimit = 100
startSurvivorsLimit = 10
survivorsLimit = startSurvivorsLimit
endSurvivorsLimit = 78
# endSurvivorsLimit = 48
# endSurvivorsLimit = 96
startEliteLimit = 0
eliteLimit = startEliteLimit
endEliteLimit = 22
# endEliteLimit = 52
# endEliteLimit = 0
turnsLimit = 100
generationsLimit = 250
# generationsLimit = 250
# genomeLength = 12
genomeLength = 5
numberOfMutations = 1
mutationRate = 0.05
visualizeRate = 2
crossoverProbability = 0.3

if endEliteLimit > 0:
    eliteChangeRate = int(generationsLimit / ((endEliteLimit - startEliteLimit) / 2))
else:
    eliteChangeRate = 2
survivorChangeRate = int(generationsLimit / ((endSurvivorsLimit - startSurvivorsLimit) / 2))
# print("tohle")
# print(eliteChangeRate,survivorChangeRate)
# input()

startingposition = [8, 1]
map = space.initMap(width, height)
initialPopulation = []
for i in range(0, popLimit):
    initialPopulation.append(individual.Snake(width, height, turnsLimit, startingposition, genomeLength))

generationID = 0
currentPopulation = initialPopulation
doc = []
for i in range(0, generationsLimit + 1):


    # getting more and more precise results
    if generationID % survivorChangeRate == 0:
        if survivorsLimit + 2 <= endSurvivorsLimit:
            survivorsLimit += 2
    # getting more and more precise results
    if generationID % eliteChangeRate == 0:
        if eliteLimit + 2 <= endEliteLimit:
            eliteLimit += 2

    heuristics = []
    n = 0
    aver = 0
    for x in currentPopulation:
        heur = x.simulate()
        aver += heur
        heuristics.append([heur, n])
        n += 1
    heuristics.sort(reverse=True)
    aver = float(aver) / float(n)
    elite = []
    heur2 = 0
    for j in range(0, eliteLimit):
        heur2 += heuristics[j][0]
        elite.append(copy.deepcopy(currentPopulation[heuristics[j][1]]))
    # avgOfElite = int(heur2/eliteLimit)
    # doc.append(avgOfElite)
    # deepBest = copy.deepcopy(currentPopulation[heuristics[0][1]])
    best = currentPopulation[heuristics[0][1]]

    # for statistical purposes
    # print(best.fitness)
    # print(aver)
    doc.append(aver)

    # visualization
    if generationID % visualizeRate == 0:
        # print("sur a elite: ",survivorsLimit,eliteLimit)
        # input()
        print("heur bude: ", heuristics[0][0])
        # input()
        # print(best.result)
        best.visualize(generationID,aver)

    # natural selection
    survivors, test = population.getSurvivors(currentPopulation, heuristics, survivorsLimit)

    # old natural selection
    # survivors = []
    # for j in range(0, survivorsLimit):
    #     survivors.append(currentPopulation[heuristics[j][1]])

    # print(test)
    # input()

    # crossover
    # children = survivors
    children = population.crossoverPopulation(survivors, genomeLength, crossoverProbability)

    # adding best - elitism with mutation
    for j in range(0, eliteLimit):
        children.append(elite[j])

    # mutation
    # mutated = children
    mutated = population.mutatePopulation(children, numberOfMutations, mutationRate)

    # filling remaining space with randoms
    # -1 if elitism
    newPopulation = mutated
    for j in range(0, (popLimit - survivorsLimit) - eliteLimit):
        # for j in range(0, (popLimit - survivorsLimit)):
        newPopulation.append(individual.Snake(width, height, turnsLimit, startingposition, genomeLength))

    # adding best - elitism without mutation
    # newPopulation.append(deepBest)
    # for j in range(0,eliteLimit):
    #     newPopulation.append(elite[j])

    # testing correct size of population
    if int((generationID / generationsLimit) * 100) % 2 == 0:
        print(int((generationID / generationsLimit) * 100), "%")
    # print(len(newPopulation))
    # input()

    currentPopulation = newPopulation
    generationID += 1

print("wtfffffffff")
print(survivorsLimit,eliteLimit)
input()

statistic_file = os.path.join(os.getcwd(), 'statistic')
statisticFile = open(statistic_file, "w+")
for x in doc:
    line = str(x) + "\n"
    statisticFile.write(line)
statisticFile.close()
