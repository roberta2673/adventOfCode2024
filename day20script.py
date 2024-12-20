from itertools import combinations
import utils as u
import table as t
import heapq

def findDist(start):
    dist = {start: 0}
    queue= [start]
    while queue:
        pos = queue.pop()
        for newPos, value in table.findNeighbours(pos): 
            if value != "#" and newPos not in dist.keys():
                dist[newPos] = dist[pos] + 1
                queue.append(newPos)
    return dist

def main():
    global table
    input, st = u.getInput("20") 
    table = t.Table(input)
    start = table.getPos("S") [0] 
    dist = findDist(start)
    count = 0
    
if __name__ == "__main__":
    exit(main())
