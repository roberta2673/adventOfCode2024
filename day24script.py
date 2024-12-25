import utils as u
import re

def main():
    input, st = u.getInput("24", False)
    values = input.split("\n\n")[0].splitlines()
    conn = input.split("\n\n")[1].splitlines()
    res = {}
    for value in values:
        key, v = value.split(": ")
        res[key] = int(v)
    while conn:
        co = conn.pop(0)
        a, ope, b, _, c = co.split()
        if a in res.keys() and b in res.keys():
            match(ope):
                case "AND":
                    res[c] = int(res[a] & res[b])
                case "OR":
                    res[c] = int(res[a] | res[b])
                case "XOR":
                    res[c] = int(res[a] ^ res[b])
        else:
            conn.append(co)
    sortedKeys = reversed(sorted(res.keys()))
    num = ""
    for key in sortedKeys:
        if key.startswith("z"):
            num += str(res[key])
    print(num, int(num,2))
    first = ""
    sortedKeys = reversed(sorted(res.keys()))
    for key in sortedKeys:
        if key.startswith("x"):
            first += str(res[key])
    first = first[-5:]
    print(first, int(first,2))
    sortedKeys = reversed(sorted(res.keys()))
    second = ""
    for key in sortedKeys:
        if key.startswith("y"):
            second += str(res[key])
    second=second[-5:]
    print(second, int(second,2))
    target = bin(int(first,2) + int(second, 2))[-5:]
    print(target)
        

if __name__ == "__main__":
    exit(main())
