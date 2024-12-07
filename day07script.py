from itertools import product
import utils as u

def isValid(res, numbers, part2 = False):
    queue = [numbers]
    while queue:
        numList = queue.pop()
        if len(numList)==1 and numList[0] == res:
            return True
        if len(numList) > 1:
            queue.append(([numList[0]+numList[1]] + numList[2:]))
            queue.append(([numList[0]*numList[1]] + numList[2:]))
            if part2:
                queue.append(([int(str(numList[0])+str(numList[1]))] + numList[2:]))
    return False

def main():
    global input
    input, st = u.getInput("07")
    eq = {}
    sum1, sum2 = 0, 0
    for line in input:
        result = int(line.split(": ")[0])
        numbers = [int(n) for n in line.split(": ")[1].split()]
        eq.update({result: numbers})
        if isValid(result, numbers):
            sum1+=result
        elif isValid(result, numbers, True):
            sum2 += result      
    u.result(sum1, 1985268524462, st)
    u.result(sum1 + sum2, 150077710195188, st)
    
if __name__ == "__main__":
    exit(main())
