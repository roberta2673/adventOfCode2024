import utils as u
import table as t

class Num():
    def __init__(self, pos, len): 
        self.pos = pos
        self.len = len
        
    def val(self): 
        return (2*self.pos + self.len-1) * self.len // 2

def main():
    global table, antennas
    input, st = u.getInput("09", False)
    string = []
    freespace = False
    count = 0
    ##for i, n in enumerate(input):
    ##    if not freespace:
    ##        string += [count] * int(n)
    ##        count += 1
    ##    else:
    ##        string += ["."] * int(n)
    ##    freespace = not freespace
    ##nPoints = string.count(".")
    ##split = len(string) - nPoints
    ##numbersToMove = [x for x in string[split:len(string)] if x != "."]
    ##while numbersToMove:
    ##    string[string.index(".")] = numbersToMove.pop()
    ##string = string[:split] + ["."] * nPoints
    ##sum = 0
    ##for i, s in enumerate(string[:split]):
    ##    sum += i*int(s)
    ##print(sum)
    pos, num = 0, []
    for len in map(int, input):
        num += [Num(pos, len)]
        pos += len

    for used in num[::-2]:
        for free in num[1::2]:
            if (free.pos <= used.pos and free.len >= used.len):
                used.pos  = free.pos
                free.pos += used.len
                free.len -= used.len

    print(sum(id*m.val() for id, m in enumerate(num[::2])))
    
    pos, num = 0, []
    for len in map(int, input):
        num += [Num(pos, len)]
        pos += len

    for used in num[::-2]:
        for free in num[1::2]:
            if (free.pos <= used.pos and free.len >= used.len):
                used.pos  = free.pos
                free.pos += used.len
                free.len -= used.len

    print(sum(id*m.val() for id, m in enumerate(num[::2])))
        
if __name__ == "__main__":
    exit(main())
