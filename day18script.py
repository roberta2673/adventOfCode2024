import utils as u
import table as t

def findMin(start, end, p2 = False):
    dist = {start: 0}
    queue= set()
    queue.add((0, start))
    minScore = 1e4
    while queue: 
        score, pos = queue.pop()
        if pos == end and score <= minScore:
            minScore = min(score, minScore)
            if p2:
                return minScore
            continue
        if dist[pos] > score:
            continue
        for newPos, value in table.findNeighbours(pos): 
            if value == "." and (newPos not in dist.keys() or score <= dist[newPos]): 
                dist[newPos] = score + 1
                queue.add((score+1, newPos))
    return minScore
    
def main():
    global table
    input, st = u.getInput("18")
    blocks = []
    for line in input:
        x,y = line.removesuffix("\n").split(",")
        blocks.append((int(x),int(y)))
    xMax = max([x for x,_ in blocks])
    yMax = max([y for _,y in blocks])
    table = t.createEmptyTable(xMax+1, yMax+1, ".")
    for b in blocks[:1024]:
        table.setValue(b,"#")
    u.result(findMin((0,0),(xMax, yMax)), 384, st)
    for b in blocks[1024:]:
        table.setValue(b, "#")
        if findMin((0,0),(xMax, yMax), True) == 1e4:
            u.result(b, (36,10), st)
            break
        
    
    
if __name__ == "__main__":
    exit(main())
