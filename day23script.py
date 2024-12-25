import utils as u

def add(groups, n1, n2, n3):
    if (n1, n2, n3) not in groups:
        if (n1, n3, n2) not in groups:
            if (n2, n1, n3) not in groups:
                if (n2, n3, n1) not in groups:
                    if (n3, n1, n2) not in groups:
                        if (n3, n2, n1) not in groups:
                            groups.append((n1, n2, n3))
        
def main():
    input, st = u.getInput("23") 
    connectons = []
    groups = []
    for line in input:
        connectons.append((line.split("-")[0], line.removesuffix("\n").split("-")[1]))
    for (a,b) in connectons:
        for (c,d) in connectons:
            for (e,f) in connectons:
                g = set()
                g.add(a)
                g.add(b)
                g.add(c)
                g.add(d)
                g.add(e)
                g.add(f)
                g = list(g)
                if len(g) == 3:
                    print(g)
                    add(groups, g[0], g[1], g[2])
    print(groups)
    
if __name__ == "__main__":
    exit(main())
