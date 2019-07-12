import os
import time

clear = lambda: os.system('clear')

def initMap(width, height):
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
    return arr


def show(arr, height, width, delay):
    clear()
    for i in range(height):
        for q in range(width):
            if (arr[i][q] == 0):
                print(" ", end="")
            elif (arr[i][q] == 1):
                print('\033[m' + "S" + '\033[0m', end="")
            elif (arr[i][q] == 2):
                print('\033[1m' + "#" + '\033[0m', end="")
            elif (arr[i][q] == 3):
                print('\033[93m' + '\033[1m' + "*" + '\033[0m', end="")
            # elif (arr[i][q] == 5):
            #     print("%", end="")
        print("")
    # time.sleep(delay)
