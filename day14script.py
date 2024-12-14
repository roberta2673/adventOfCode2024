from itertools import product
from math import floor
import utils as u
import table as t

def getRobots():
    robots = []
    for line in input:
        line = line.removesuffix("\n")
        (x,y) = [int(n) for n in line.split()[0].split("=")[1].split(",")]
        (vx,vy) = [int(n) for n in line.split()[1].split("=")[1].split(",")]
        robots.append((x, y, vx, vy))
    return robots
        
def getEndPos(iter):
    end = []
    for (x, y, vx, vy) in robots:
        xend = x + vx*iter % xMax
        if xend >= xMax:
            xend = xend - xMax
        if xend < 0:
            xend = xMax + xend
        yend = y + vy*iter % yMax
        if yend >= yMax:
            yend = yend - yMax
        if yend < 0:
            yend = yMax + yend
        end.append((xend, yend))
    return end

def getQuadrantsProd(end):
    q = [0, 0, 0, 0]
    xmax2 = floor((xMax)/2)
    ymax2 = floor((yMax)/2)
    for (xend, yend) in end:
        if xend < xmax2 and yend < ymax2:
            q[0] +=1
        elif xend > xmax2 and yend < ymax2:
            q[1] +=1
        elif xend < xmax2 and yend > ymax2:
            q[2] +=1
        elif xend > xmax2 and yend > ymax2:
            q[3] +=1
    return q[0]*q[1]*q[2]*q[3]

def display(end): # Only for easter egg!
    table = t.createEmptyTable(xMax, yMax, ".")
    for e in end:
        table.setValue(e, "#")
    print(table) 
    
def getTreePos():
    for i in range(10000):
        end = getEndPos(i)
        if len(end) == len(set(end)):
            display(end)
            return i
    
def main():
    global input, robots, xMax, yMax
    input, st = u.getInput("14")
    robots = getRobots()
    xMax = max(x for x,_,_,_ in robots) + 1
    yMax = max(y for _,y,_,_ in robots) +1
    end = getEndPos(100)
    u.result(getQuadrantsProd(end), 221142636, st)
    u.result(getTreePos(), 7916, st) 
    
if __name__ == "__main__":
    exit(main())
