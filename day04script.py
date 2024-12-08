import utils as u
import table as t

def getXmas():
    count = 0
    XMAS = ["X", "M", "A", "S"]
    for (x, y) in table.getPos("X"):
        for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0 , 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]:
            if all(table.getValue((x+dx*i, y+dy*i)) == XMAS[i] for i in range(1,4)):
                count +=1  
    return count

def getXmas2(): 
    count = 0
    for (x, y) in table.getPos("A"):
        neigh = [table.getValue((x+dx, y+dy)) for (dx, dy) in [(-1, -1), (1, -1), (-1, 1), (1, 1)]]
        if neigh.count("M") == 2 and neigh.count("S") == 2 and neigh[0] != neigh[3] and neigh[1] != neigh[2]: 
                count+=1
    return count

def main():
    global table
    input, st = u.getInput("04")
    table = t.Table(input)
    u.result(getXmas(), 2593, st)
    u.result(getXmas2(), 1950, st)
    
if __name__ == "__main__":
    exit(main())
