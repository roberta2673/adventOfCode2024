import utils as u
import table as t

numeric = {"7":(0,0), "8":(1,0), "9":(2,0), "4":(0,1), "5":(1,1), "6":(2,1), "1":(0,2), "2":(1,2), "3":(2,2), "0":(1,3), "A":(2,3)}
directional = {"^":(1,0), "A":(2,0), "<": (0,1), "v":(1,1), ">":(2,1)}
dirToStr = {(0,-1):"^", (-1,0):"<", (0,1):"v", (1,0):">"}
    
def move(path, target, nPos, dPos):
    nShift = (numeric[target][0]-nPos[0], numeric[target][1]-nPos[1])
    if (nPos[0] + nShift[0]) == 0:
        if nShift[1]:           
            path, dShift = click(path, dirToStr[(0,int(nShift[1]/abs(nShift[1])))], dPos)
            dPos = (dPos[0]+dShift[0], dPos[1]+dShift[1])
            path+="A"*(abs(nShift[1])-1)
        if nShift[0]:
            path, dShift = click(path, dirToStr[(int(nShift[0]/abs(nShift[0])),0)], dPos)
            dPos = (dPos[0]+dShift[0], dPos[1]+dShift[1])
            path+="A"*(abs(nShift[0])-1)
    else:
        if nShift[0]:
            path, dShift = click(path, dirToStr[(int(nShift[0]/abs(nShift[0])),0)], dPos)
            dPos = (dPos[0]+dShift[0], dPos[1]+dShift[1])
            path+="A"*(abs(nShift[0])-1)
        if nShift[1]:           
            path, dShift = click(path, dirToStr[(0,int(nShift[1]/abs(nShift[1])))], dPos)
            dPos = (dPos[0]+dShift[0], dPos[1]+dShift[1])
            path+="A"*(abs(nShift[1])-1)
    nPos = (nPos[0]+nShift[0], nPos[1]+nShift[1])
    return path, nPos, dPos

def click(path, target, dPos):
    dShift = (directional[target][0]-dPos[0], directional[target][1]-dPos[1])
    if (dPos[0] + dShift[0]) == 0:
        if dShift[1]!=0:
            path+=dirToStr[(0,int(dShift[1]/abs(dShift[1])))]*abs(dShift[1])
        if dShift[0]!=0:
            path+=dirToStr[(int(dShift[0]/abs(dShift[0])), 0)]*abs(dShift[0])
    else:
        if dShift[0]!=0:
            path+=dirToStr[(int(dShift[0]/abs(dShift[0])), 0)]*abs(dShift[0])
        if dShift[1]!=0:
            path+=dirToStr[(0,int(dShift[1]/abs(dShift[1])))]*abs(dShift[1])
    path+="A"
    return path, dShift

def main():
    global table
    input, st = u.getInput("21")
    res = 0
    for line in input:
        line = line.removesuffix("\n")
        path = ""
        nPos = numeric["A"]
        for n in line:
            dPos = directional["A"]
            path, nPos, dPos = move(path, n, nPos, dPos)
            path, _ = click(path, "A", dPos)
            path1 = ""
            dPos = numeric["A"]
            d1Pos = directional["A"]
            for p in path:
                path1, dShift = click(path1, p, d1Pos)
                d1Pos = (d1Pos[0]+dShift[0], d1Pos[1]+dShift[1])
        print(line, path)
        print(len(path1), path1)
        res += (len(path1)*int(line.replace("A","")))
    print(res)

                
if __name__ == "__main__":
    exit(main())
