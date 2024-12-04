def createEmptyTable(dim, emptyValue):
    return Table([str(emptyValue)*dim + "\n"] * dim)

class Table:
    def __init__(self, input):
        self.data = []
        for y, line in enumerate(input):
            line = line.removesuffix("\n")
            self.data.append([])
            for value in line:
                self.data[y].append(value)
        self.height = len(self.data)
        self.width = len(self.data[0])

    def getValues(self):
        values = {}
        for y, line in enumerate(self.data):
            for x, value in enumerate(line):
                values.update({(x,y): value})
        return values.items()

    def setValue(self, pos, new_value):
        (x,y) = pos
        self.data[y][x] = new_value
    
    def incrValue(self, pos):
        value = int(self.getValue(pos))
        self.setValue(pos, value+1)
        
    def getValue(self, pos):
        (x,y) = pos
        if x in range(0, self.width) and y in range(0, self.height):
            return self.data[y][x]
        else:
            return False
    
    def getPos(self, v):
        posList = []
        for y, line in enumerate(self.data):
            for x, value in enumerate(line):
                if value == v:
                    posList.append((x,y))
        return posList
    
    def findNeighbours(self, pos, conn = 4):
        (x,y) = pos
        neigh = {}
        neighPos = [(x-1, y), (x+1, y), (x,y-1), (x,y+1)]
        if (conn == 8):
            neighPos += [(x-1, y-1), (x+1, y-1), (x-1,y+1), (x+1,y+1)]
        for (xn, yn) in neighPos:
            value = self.getValue((xn,yn))
            if value:
                neigh.update({(xn,yn):value})
        return neigh.items()
    
    def findROI(self, xi, xf, yi, yf):
        roi = {}
        for yn in range(yi,yf+1):
            for xn in range(xi, xf+1):
                value = self.getValue((xn,yn))
                if value:
                    roi.update({(xn,yn):value})
        return roi

    def getRow(self, row):
        return self.data[row]
    
    def getColumn(self, column):
        return [self.data[y][column] for y in range(0, self.height)]

    def rotateTable(self):
        rotatedTable = self
        for (x,y), value in self.getValues():
            rotatedTable.setValue((y,x), value)
        return rotatedTable
    
    def compareTable(self, other):
        for y, line in enumerate(self.data):
            for x, value in enumerate(line):
                if not other.data[y][x] == value:
                    return False
        return True
    
    def __str__(self) -> str:
        s = ""
        for line in  self.data:
            s += "".join([str(x) for x in line]) + "\n"
        return s