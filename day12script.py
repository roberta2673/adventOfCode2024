import utils as u
import table as t
        
class Region():
    def __init__(self, value, pos):
        self.value = value
        self.pos = pos
    
    def getPerimeter(self):
        perimeter = set()
        for (x, y) in self.pos:
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (x+dx, y+dy) not in self.pos:
                    perimeter.add(((x,y),(x+dx, y+dy)))
                    continue
        return perimeter
    
    def getBounds(self):
        perimeter = set(self.getPerimeter())
        bounds = set()
        for (l1x, l1y), (l2x, l2y) in perimeter:
            if ((l1x+1, l1y),(l2x+1, l2y)) not in perimeter and ((l1x, l1y+1),(l2x, l2y+1)) not in perimeter:
                bounds.add(((l1x, l1y),(l2x,l2y)))
        return len(bounds)

def main():
    global table
    input, st = u.getInput("12")
    table = t.Table(input)
    regions = []
    toCheck = [(x,y) for x in range(table.width) for y in range(table.height)]
    while toCheck:
        pos = toCheck.pop()
        value = table.getValue(pos)
        queue = [pos]
        visited = [pos]
        while queue:
            curr = queue.pop()
            for npos, nvalue in table.findNeighbours(curr):
                if nvalue == value and npos not in visited:
                    visited.append(npos)
                    toCheck.remove(npos)
                    queue.append(npos)
        regions.append(Region(value, visited))
    u.result(sum(len(r.getPerimeter())*len(r.pos) for r in regions), 1381056, st)      
    u.result(sum(r.getBounds()*len(r.pos) for r in regions), 834828, st)                  
    
    
if __name__ == "__main__":
    exit(main())
