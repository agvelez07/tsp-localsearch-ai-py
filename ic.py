import math
import random
from code import interact

# Global variable to keep track of the next available city ID
next_id = 1


# 1. Creates a new city with incremental ID and random values as coordinates
def criarIC():
    global next_id
    city = (next_id, random.randint(1, 999), random.randint(1, 999))
    next_id += 1
    return city

# 2. Calculates distance between two cities
def distIC(iCidade1, iCidade2):
    return math.sqrt((iCidade1[1] - iCidade2[1]) ** 2 + (iCidade1[2] - iCidade2[2]) ** 2)

# 3. Creates and returns a list of n iCidades with sequential ID
def criarMultiplasIC(n):
    return [criarIC() for _ in range(n)]

# 4. Calculate the Circular Distance of a List of iCidades
def distCircularIC(ICidades):
    if len(ICidades) < 2:
        return 0

    circularDistance = 0

    for x in range(-1, len(ICidades) - 1):
        distance = distIC(ICidades[x], ICidades[x + 1])
        circularDistance += distance

    distance = distIC(ICidades[0], ICidades[-1])
    circularDistance += distance

    return circularDistance

# 6. Swap Two Cities in a New List
def successor(iCList, pos1, pos2):
    newICList = iCList.copy()
    newICList[pos1], newICList[pos2] = newICList[pos2], newICList[pos1]

    if pos1 > pos2:
        pos1, pos2 = pos2, pos1

    newICList[pos1:pos2 + 1] = reversed(newICList[pos1:pos2 + 1])

    return newICList

def trocaIC(iCList, pos1, pos2):
    newICList = iCList.copy()
    newICList[pos1], newICList[pos2] = newICList[pos2], newICList[pos1]

    return newICList

# 7. Swap Two Cities if the Distance Improves
def trocaSeMelhorIC(iCList):
    newICList = iCList.copy()
    pos1 = random.randint(0, len(newICList) - 1)
    while True:
        pos2 = random.randint(0, len(newICList) - 1)
        if pos2 != pos1:
            break

    newICList[pos1], newICList[pos2] = newICList[pos2], newICList[pos1]

    iCListDistance = distCircularIC(iCList)
    newICListDistance = distCircularIC(newICList)

    if newICListDistance <= iCListDistance:
        return newICList
    else:
        return iCList

    # 8. Improve Circular Distance by Applying the Swap Function r Times

def melhoraDistCircularIC(iCList, r):
    newICList = iCList.copy()
    for _ in range(r):
        newICList = trocaSeMelhorIC(newICList)
    return newICList

# 9. Optimize Circular Distance and Return Initial Distance, New Distance, and Optimized List
def optDistCircularIC(iCList, r):
    listCircularDist = distCircularIC(iCList)

    optimizedList = melhoraDistCircularIC(iCList, r)

    newlistCircularDist = distCircularIC(optimizedList)

    return listCircularDist, newlistCircularDist, optimizedList

def smartShuffle(iCList, swaps=20):
    shuffled = iCList.copy()
    n = len(shuffled)
    for _ in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
    return shuffled

def successor(iCList, pos1, pos2):
    newICList = iCList.copy()
    newICList[pos1], newICList[pos2] = newICList[pos2], newICList[pos1]

    if pos1 > pos2:
        pos1, pos2 = pos2, pos1

    newICList[pos1:pos2 + 1] = reversed(newICList[pos1:pos2 + 1])
    return newICList

def greedy(iCList, r):
    currentList = smartShuffle(iCList, swaps=20)
    currentDist = distCircularIC(currentList)
    maxStagnantIterations = max(1, int(0.1 * r))

    for _ in range(r):
        if maxStagnantIterations == 0:
            continue

        improved = False
        bestDist = currentDist
        bestList = currentList

        for i in range(len(currentList)):
            for j in range(i + 1, len(currentList)):
                tempList = successor(currentList, i, j)
                tempDist = distCircularIC(tempList)

                if tempDist < bestDist:
                    bestDist = tempDist
                    bestList = tempList
                    improved = True

        if not improved:
            maxStagnantIterations -= 1
        else:
            currentList = bestList
            currentDist = bestDist

    return distCircularIC(iCList), currentDist, currentList

def sGreedy(iCList, r):
    b = 100

    currentList = smartShuffle(iCList, swaps=20)
    currentDist = distCircularIC(currentList)
    maxStagnantIterations = max(1, int(0.1 * r))

    for _ in range(r):
        if maxStagnantIterations == 0:
            continue

        improved = False
        successors = []

        for i in range(len(currentList)):
            for j in range(i + 1, len(currentList)):
                tempList = successor(currentList, i, j)
                tempDist = distCircularIC(tempList)

                if tempDist < currentDist:
                    successors.append((tempDist, tempList))
                    improved = True

        if not improved or not successors:
            maxStagnantIterations -= 1
            continue

        result = sorted(successors, key=lambda x: x[0])
        top = result[:b] if len(result) >= b else result
        chosenDist, chosenList = random.choice(top)

        currentList = chosenList
        currentDist = chosenDist

    return distCircularIC(iCList), currentDist, currentList

def pGreedy(iCList, r):
    currentList = smartShuffle(iCList, swaps=20)
    currentDist = distCircularIC(currentList)
    n = len(currentList)
    maxStagnantIterations = max(1, int(0.1 * r))

    for _ in range(r):
        if maxStagnantIterations == 0:
            continue

        improved = False
        bestDist = currentDist
        bestList = currentList

        for _ in range(n):
            j = random.randint(0, n - 1)
            k = random.randint(0, n - 2)
            if k >= j:
                k += 1

            tempList = successor(currentList, j, k)
            tempDist = distCircularIC(tempList)

            if tempDist < bestDist:
                bestDist = tempDist
                bestList = tempList
                improved = True

        if not improved:
            maxStagnantIterations -= 1
        else:
            currentList = bestList
            currentDist = bestDist

    return distCircularIC(iCList), currentDist, currentList

def rGreedy(iCList, r):
    iterCount = 2
    restartsLeft = r
    restartCount = 0

    bestList = None
    bestDist = float('inf')

    while restartsLeft >= iterCount:
        _, dist, candidate = pGreedy(iCList, iterCount)
        if dist < bestDist:
            bestDist = dist
            bestList = candidate

        restartsLeft -= iterCount
        iterCount *= 2
        restartCount += 1

    if restartsLeft > 0:
        _, dist, candidate = pGreedy(iCList, restartsLeft)
        if dist < bestDist:
            bestDist = dist
            bestList = candidate
        restartCount += 1

    return distCircularIC(iCList), bestDist, bestList

"""
# Generate 5 Cities
iCidades = criarMultiplasIC(5)

# Run Distance Calculation
distCircularIC(iCidades)

# Swap Cities
iCidades = trocaIC(iCidades, 0, 1)

# Swap If Better
iCidades = trocaSeMelhorIC(iCidades)

# Improve Distance with Multiple Swaps
iCidades = melhoraDistCircularIC(iCidades, 4)

# Optimize and Return All Values
initial_dist, optimized_dist, optimized_list = optDistCircularIC(iCidades)
print("\nFinal Optimized List:")
printCitiesInCityList(optimized_list)
"""
