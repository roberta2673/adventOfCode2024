import utils as u
from sympy import solve, Symbol

def getMinPrice(block, offset = 0):
    match = u.solveRegex(block, "Button A: X\+(\d+)\, Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X\=(\d+), Y\=(\d+)")
    ax, ay = (int(match[0]), int(match[1]))
    bx, by = (int(match[2]), int(match[3]))
    tx, ty = (int(match[4]) + offset, int(match[5]) + offset)
    na = Symbol("na", integer=True)
    nb = Symbol("nb", integer=True)         
    roots = solve(
        [na * ax + nb * bx - tx, na * ay + nb * by - ty],
        [na, nb],
    )
    return roots[na] * 3 + roots[nb] if roots else 0

def main():
    input, st = u.getInput("13", False)
    u.result(sum(getMinPrice(block) for block in input.split("\n\n")), 32067, st)
    u.result(sum(getMinPrice(block, 10000000000000) for block in input.split("\n\n")), 92871736253789, st)
    
if __name__ == "__main__":
    exit(main())
