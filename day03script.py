import utils as u
import re

def main():
    input, st = u.getInput("03", False)
    sum1 = sum2 = 0
    enabled = True
    for a, b, do, dont in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", input):
        if do or dont:
            enabled = bool(do)
        else:
            x = int(a) * int(b)
            sum1 += x
            sum2 += x * enabled
    u.result(sum1, 168539636, st)
    u.result(sum2, 97529391, st)

if __name__ == "__main__":
    exit(main())
