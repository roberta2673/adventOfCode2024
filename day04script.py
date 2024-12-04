import utils as u
import table as t

def getXmas():
    xmas = 0
    for (x, y) in table.getPos("X"):
        for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0 , 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]:
            if table.getValue((x+dx*3, y+dy*3)) == "S" and table.getValue((x+dx*2, y+dy*2)) == "A" and table.getValue((x+dx, y+dy)) == "M":
                xmas +=1  
    return xmas

def getXmas2(): 
    xmas = 0
    for (x, y) in table.getPos("A"):
        neigh = []
        for (dx, dy) in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
            neigh.append(table.getValue((x+dx, y+dy)))
        if neigh.count("M") == 2 and neigh.count("S") == 2 and neigh[0] != neigh[3] and neigh[1] != neigh[2]: 
                xmas+=1
    return xmas

def main():
    global table
    input, st = u.getInput("04")
    table = t.Table(input)
    u.result(getXmas(), 2593, st)
    u.result(getXmas2(), 1950, st)
    
if __name__ == "__main__":
    exit(main())
