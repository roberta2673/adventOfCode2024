import re
import math
import time

def getInput(i, splitLines = True):
    startTime = time.time()
    file = open(f".\\day{i}input.txt")
    if splitLines:
        input = file.readlines()
    else:
        input = file.read()
    file.close()
    return input, startTime

def result(result, expected, startTime):
    endTime = time.time()
    print("Result:", result, ", time:", round(endTime-startTime, 4))
    assert result == expected

def solveRegex(text: str, regex):
    matches = re.findall(regex, text.removesuffix("\n"), re.MULTILINE)
    if len(matches)>0:
        return matches[0]
    else:
        return False

def solveSecondDegreeEq(a, b, c):
    delta = math.sqrt(b**2-4*a*c)
    x1 = (-b-delta)/2*a
    x2 = (-b+delta)/2*a
    return x1, x2


# Teorema di Gauss
# Area di un poligono
# A = 0.5 * | Ʃ(x_i *y_i+1 -x_i+1 *y_i) |
def getGaussArea(boundary):
    sum=0
    for i in range(0, len(boundary)):
        sum += boundary[i-1][0]*boundary[i][1] - boundary[i][0]*boundary[i-1][1]
    return 0.5 *abs(sum)

# Pick's theorem 
    #   i = A - b / 2 + 1
    #       i: the number of integer points interior to the polygon     [?]
    #       A: polygon's area                                           [with Gauss theorem]
    #       b: number of integer points on its boundary                 [len(boundary_cells)]
def getPicksNumber(boundary, lenBoundary):
    return int(getGaussArea(boundary) - lenBoundary / 2 + 1)

