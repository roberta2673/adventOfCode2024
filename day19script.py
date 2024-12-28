from functools import cache
import utils as u

@cache
def getComb(d):
    comb = 0
    if not d:
        return 1
    for p in patterns:
        if d.startswith(p):
            comb+=getComb(d[len(p):])
    return comb

def main():
    global patterns
    input, st = u.getInput("19", False)
    patterns = input.split("\n\n")[0].split(", ")
    designs = input.split("\n\n")[1].splitlines()
    comb = [getComb(d) for d in designs]
    u.result(len([c for c in comb if c>0]), 247, st)
    u.result(sum(comb), 692596560138745, st)    
    
if __name__ == "__main__":
    exit(main())