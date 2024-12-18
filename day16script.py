import utils as u
import table as t
import heapq

def findMin(start, end):
    dist = {(start, (0,1)): 0}
    queue= [(0, start, (0, 1), [start])]
    minScore = 1e7
    best = []
    while queue: 
        score, pos, dir, path = heapq.heappop(queue)
        if pos == end and score <= minScore:
            minScore = min(score, minScore)
            best += path
            continue
        if dist[(pos, dir)] > score:
            continue
        for newPos, value in table.findNeighbours(pos): 
            newDir = (newPos[0]-pos[0], newPos[1]-pos[1])
            if value != "#" and ((newPos, newDir) not in dist.keys() or score <= dist[(newPos, newDir)]): 
                p = 1 if dir == newDir else 1001
                dist[(newPos, newDir)] = score + p
                heapq.heappush(queue, (score + p, newPos, newDir, path + [newPos]))
    return minScore, len(set(best))
    
def main():
    global table
    input, st = u.getInput("16") 
    table = t.Table(input)
    start = table.getPos("S") [0] 
    end = table.getPos("E")[0] 
    minScore, nBest = findMin(start, end)
    u.result(minScore, 107468, st)
    u.result(nBest, 533, st)
    
    
if __name__ == "__main__":
    exit(main())
