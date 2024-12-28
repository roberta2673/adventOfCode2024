import utils as u
import table as t

dirMap = {"<": (-1,0), ">": (1,0), "^": (0,-1), "v": (0,1)}
    
def getBoxes(table):
    (x, y) = table.getPos("@")[0]
    for dir in dirs:
        table.setValue((x, y), ".")
        dx, dy = dirMap[dir]
        n = 1
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
        n = 1
        if dy == 0:
            while table.getValue((x+dx*n, y+dy*n)) == "[" or table.getValue((x+dx*n, y+dy*n)) == "]":
                n+=1
            if table.getValue((x+dx*n, y+dy*n)) == ".":
                for i in reversed(range(1,n+1)):
                    table.copyValue((x+dx*i, y+dy*i), (x+dx*(i-1), y+dy*(i-1)))
                x += dx
                y += dy   
        else:
            pyramid = [[0]]
            while any([table.getValue((x+size, y+dy*n)) in ["[", "]"] for size in pyramid[-1]]) and all([table.getValue((x+size, y+dy*n)) != "#" for size in pyramid[-1]]):
                layer = set()
                for l in pyramid[-1]:
                    match(table.getValue((x+l, y+dy*n))):
                        case "[":
                            layer.add(l)
                            layer.add(l+1)
                        case "]":
                            layer.add(l)
                            layer.add(l-1)
                pyramid.append(layer)
                n+=1
            pyramid.append(pyramid[-1])
            if all([table.getValue((x+size, y+dy*n)) == "." for size in pyramid[-1]]):
                for i in reversed(range(1,n+1)):
                    for size in pyramid[i-1]:
                        table.moveValue((x+size, y+dy*i), (x+size, y+dy*i-dy))
                x += dx
                y += dy       
        table.setValue((x, y), "@")
    return table.getPos("[")

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
            if n == "#" or n == ".":
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
    u.result(sum([x+y*100 for x, y in getBoxes2(table)]), 1432781, st)
    
if __name__ == "__main__":
    exit(main())
