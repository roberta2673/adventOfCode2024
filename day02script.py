import utils as u

def ascCheck(levels):
    n1 = int(levels[0])
    n2 = int(levels[round(len(levels)/2)])
    n3 = int(levels[-1])
    return all([n2 > n1, n3 > n1, n3 > n2])
    
def safeCheck(levels):
    asc = ascCheck(levels)
    for n in range (0, len(levels)-1):
        l1 = int(levels[n])
        l2 = int(levels[n+1])
        if not((asc and l2-l1 in range(1,4)) or (not asc and l1-l2 in range(1,4))):
            return False
    return True

def countSafes(toll = False):
    count = 0
    for line in input:
        levels = line.split()
        if safeCheck(levels):
            count += 1
        elif toll:
            for n in range(len(levels)):
                if safeCheck(levels[:n] + levels[n+1:]):
                    count += 1
                    break
    return count    
 
def main():
    global input
    input, st = u.getInput("02")
    u.result(countSafes(), 383, st)
    u.result(countSafes(True), 436, st)
    
if __name__ == "__main__":
    exit(main())
