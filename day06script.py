import utils as u
import table as t

G = {i+j*1j: c for i,r in enumerate(open('day06input.txt'))
               for j,c in enumerate(r.strip())}

def getPath():
    pos = start
    dir = (0,-1)
    visited = set()
    while table.getValue(pos) and (pos,dir) not in visited:
        visited |= {(pos,dir)}
        newPos = (pos[0]+dir[0], pos[1]+dir[1])
        if table.getValue(newPos) == "#":
            dir = (-dir[1], dir[0])
        else: pos = newPos
    return {p for p,_ in visited}, (pos,dir) in visited

def main():
    global table, start
    input, st = u.getInput("06")
    table = t.Table(input)
    start = table.getPos("^")[0]
    visited = getPath()[0]
    u.result(len(visited), 4903, st)
    sum = 0
    for v in visited:
        table.setValue(v, "#")
        sum += getPath()[1]
        table.setValue(v, ".")
    u.result(sum, 1911, st)

if __name__ == "__main__":
    exit(main())
