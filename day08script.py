import utils as u
import table as t

def getAntennas():
    antennas = {}
    for _, value in table.getValues():
        if value != "." and value not in antennas.keys():
            antennas[value] = table.getPos(value)
    return antennas
                
def addCouple(antinodes, p1, p2, i):
    a1 = ((i+1)*p2[0]-i*p1[0], (i+1)*p2[1]-i*p1[1])
    a2 = ((i+1)*p1[0]-i*p2[0], (i+1)*p1[1]-i*p2[1])
    added = False
    for antinode in [a1, a2]:
        if table.getValue(antinode):
            antinodes.add(antinode)  
            added = True
    return added
    
def getAntinodes(noLimits = False):
    antinodes = set()
    antennas = getAntennas()
    for antenna, pos in antennas.items():
        for i, pos1 in enumerate(pos):
            if noLimits:
                antinodes.add(pos1)
            for pos2 in antennas[antenna][i+1:]:
                addCouple(antinodes, pos1, pos2, 1)
                if noLimits:
                    n = 2
                    while addCouple(antinodes, pos1, pos2, n):
                        n+=1       
    return antinodes
    
def main():
    global table, antennas
    input, st = u.getInput("08")
    table = t.Table(input)
    u.result(len(getAntinodes()), 320, st)
    u.result(len(getAntinodes(True)), 1157, st)
        
    
if __name__ == "__main__":
    exit(main())
