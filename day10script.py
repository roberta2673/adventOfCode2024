import utils as u
import table as t
    
def main():
    input, st = u.getInput("10")
    table = t.Table(input)
    trailheads = table.getPos("0")
    points = 0
    points2 = 0
    for tr in trailheads:
        valids = []
        queue = [[tr]]
        while queue:
            path = queue.pop()
            curr = path[-1]
            if table.getValue(curr) == "9":
                valids.append(path)
                continue
            neigh = table.findNeighbours(curr)
            for nPos, nVal in neigh:
                if nPos not in path and int(nVal) == int(table.getValue(curr)) +1:
                    queue.append(path+[nPos])
        points += len(set([v[-1] for v in valids]))
        points2 += len(valids)
    u.result(points, 688, st)
    u.result(points2, 1459, st)
        
             
    
if __name__ == "__main__":
    exit(main())
