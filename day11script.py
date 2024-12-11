import utils as u
from collections import defaultdict

def getStonesNum(nCycles):  
    stones = defaultdict(lambda : 0)
    for s in input.split():
        stones[s] += 1
    for _ in range (nCycles):
        newS = defaultdict(lambda : 0)
        for s , nOcc in stones.items():
            if s=="0":
                newS["1"] += nOcc
            elif len(s) % 2 == 0:
                split = int(len(s)/2)
                newS[str(int(s[:split]))] +=nOcc
                newS[str(int(s[split:]))] +=nOcc
            else:
                newS[str(int(s)*2024)] +=nOcc
        stones = newS
    return sum(stones.values())

def main():
    global input
    input, st = u.getInput("11", False)
    u.result(getStonesNum(25), 204022, st)
    u.result(getStonesNum(75), 241651071960597, st)
    
    
if __name__ == "__main__":
    exit(main())
