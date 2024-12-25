import utils as u
import table as t

def main():
    input, st = u.getInput("25", False)
    keys=[]
    pin=[]
    for schema in input.split("\n\n"):
        table = t.Table(schema.splitlines())
        new = [0]*5
        pos = table.getPos("#")
        if all([v == "#" for v in schema[:5]]):
            for i in range(0,5):
                new[i] = max([y for (x,y) in pos if x == i])
            pin.append(new)
        if all([v == "#" for v in schema[-5:]]):
            for i in range(0,5):
                new[i] = table.height - min([y for (x,y) in pos if x == i]) -1
            keys.append(new)
    count = 0
    for p in pin:
        for k in keys:
            if all([p[i] + k[i] <= 5 for i in range(0,5)]):
                count += 1
    print(count)
        

if __name__ == "__main__":
    exit(main())
