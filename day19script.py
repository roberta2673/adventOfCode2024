import utils as u
import regex as re

def createRegex(patterns):
    regex = r"^("
    for p in patterns[:-1]:
        regex += "("+p+")*|"
    regex += "("+patterns[-1]+")*)*$"
    return regex

def main():
    input, st = u.getInput("19", False)
    patterns = input.split("\n\n")[0].split(", ")
    designs = input.split("\n\n")[1].splitlines()
    print(patterns)
    points = {}
    patterns.sort(key=len, reverse=True)
    for i, p in enumerate(patterns[:-1]):
        regex = createRegex(patterns[i+1:])
        if match := re.findall(regex, p, re.MULTILINE):
            points[p] = [m for m in match[0] if m!='']
    d2 = {}
    for p, values in reversed(points.items()):
        c = 1
        for v in values:
            if v not in d2:
                c +=1
            else:
                c *=d2[v]
        d2[p] = c
    print(d2)
    regex = createRegex(patterns)
    count = 0
    for des in designs:
        match = re.findall(regex, des, re.MULTILINE)
        if match:
            c = 1
            for v in match[0]:
                if v in d2:
                    c *=d2[v]
                else:
                    c+=1
        count += c
    print(count)
    
if __name__ == "__main__":
    exit(main())

#692596560138745