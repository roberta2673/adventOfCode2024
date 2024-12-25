import utils as u
import table as t

dirMap = {"<": (-1,0), ">": (1,0), "^": (0,-1), "v": (0,1)}
    
def getBoxes(table):
    (x, y) = table.getPos("@")[0]
    for dir in dirs:
        table.setValue((x, y), ".")
        dx, dy = dirMap[dir]
        if table.getValue((x+dx, y+dy)) == ".":
            x +=dx
            y +=dy
        elif table.getValue((x+dx, y+dy)) == "O":
            n = 2
            while table.getValue((x+dx*n, y+dy*n)) == "O":
                n+=1
            if table.getValue((x+dx*n, y+dy*n)) == ".":
                table.setValue((x+dx*n, y+dy*n), "O")
                x += dx
                y += dy     
        table.setValue((x, y), "@")
    return table.getPos("O")

def getBoxes2(table):
    (x, y) = table.getPos("@")[0]
    for dir in dirs:
        table.setValue((x, y), ".")
        dx, dy = dirMap[dir]
        if table.getValue((x+dx, y+dy)) == ".":
            x +=dx
            y +=dy
        elif table.getValue((x+dx, y+dy)) == "[" or table.getValue((x+dx, y+dy)) == "]":
            if dy == 0:
                while table.getValue((x+dx*n, y+dy*n)) == "[" or table.getValue((x+dx*n, y+dy*n)) == "]":
                    n+=1
                if table.getValue((x+dx*n, y+dy*n)) == ".":
                    for i in reversed(1, n):
                        table.setValue((x+dx*i, y+dy*i), table.getValue((x+dx*(i-1), y+dy*(i-1))))
            else:
                if dy == 1:
                    check = [[(x+dx, y+dy), (x+dx+1,y+dy)]]
                    end = False
                    while not end:
                        if all(table.getValue(c) == "." for c in check[-1]):
                            
                            end = True
        table.setValue((x, y), "@")
    return table.getPos("O")

def main():
    global dirs
    input, st = u.getInput("15", False)
    table = t.Table(input.split("\n\n")[0].splitlines())
    dirs = list(input.split("\n\n")[1].replace("\n",""))
    u.result(sum([x+y*100 for x, y in getBoxes(table)]), 1406628, st)
    newInput=[]
    for line in input.split("\n\n")[0].splitlines():
        newLine = ""
        for n in line:
            if n == "#":
                newLine += n
                newLine += n
            if n == "O":
                newLine += "["
                newLine += "]"
            elif n == "@":
                newLine += n
                newLine += "."
        newInput.append(newLine)
    table = t.Table(newInput)
    print(sum([x+y*100 for x, y in getBoxes(table)]))
    
if __name__ == "__main__":
    exit(main())
