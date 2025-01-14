from functools import cache
import utils as u

numpad = {'7': (0, 0), '8': (1, 0), '9': (2, 0), '4': (0, 1), '5': (1, 1), '6': (2, 1), '1': (0, 2), '2': (1, 2), '3': (2, 2), '0': (1, 3), 'A': (2, 3)}
dirpad = {'^': (1, 0), 'A': (2, 0), '<': (0, 1), 'v': (1, 1), '>': (2, 1)}
dirToPad = {(0, 1): "v", (0, -1): "^", (1, 0): ">", (-1, 0): "<"}

def getKeypadDirs():
    keypad_dirs = {}
    for num1, loc1 in numpad.items():
       for num2, loc2 in numpad.items(): 
            dx = loc2[0]-loc1[0]
            dy = loc2[1]-loc1[1]
            xShift = "" if dx == 0 else dirToPad[(dx/abs(dx),0)]*abs(dx)
            yShift = "" if dy == 0 else dirToPad[(0,dy/abs(dy))]*abs(dy)
            if loc1[0] == 0 and loc2[1] == 3: keypad_dirs[(num1, num2)] = xShift + yShift
            elif loc1[1] == 3 and loc2[0] == 0: keypad_dirs[(num1, num2)] = yShift + xShift
            else: keypad_dirs[(num1, num2)] = [xShift, yShift]
    for dir1, loc1 in dirpad.items():
        for dir2, loc2 in dirpad.items():
            dx = loc2[0]-loc1[0]
            dy = loc2[1]-loc1[1]
            xShift = "" if dx == 0 else dirToPad[(dx/abs(dx),0)]*abs(dx)
            yShift = "" if dy == 0 else dirToPad[(0,dy/abs(dy))]*abs(dy)
            if loc1[0] == 0 and loc2[1] == 0: keypad_dirs[(dir1, dir2)] = xShift + yShift
            elif loc1[1] == 0 and loc2[0] == 0: keypad_dirs[(dir1, dir2)] = yShift + xShift
            else: keypad_dirs[(dir1, dir2)] = [xShift, yShift]
    return keypad_dirs

@cache
def click(path, level, nRob):
    if level == nRob:
        return len(path)
    else:
        n = 0
        for i, c in enumerate(path):
            dirs = keypad_dirs[('A' if i == 0 else path[i - 1], c)]
            if isinstance(dirs, list):
                n += min(click(dirs[0] + dirs[1] + 'A', level + 1, nRob), click(dirs[1] + dirs[0] + 'A', level + 1, nRob))
            else:
                n+= click(dirs + 'A', level + 1, nRob)
    return n

def main():
    global keypad_dirs, known_sequences
    input, st = u.getInput("21", False)
    keypad_dirs = getKeypadDirs()
    known_sequences = {}
    u.result(sum([click(line, 0, 3)*int(line[:-1]) for line in input.split()]), 105458, st)
    known_sequences = {}
    u.result(sum([click(line, 0, 26)*int(line[:-1]) for line in input.split()]), 129551515895690, st)

                
if __name__ == "__main__":
    exit(main())
