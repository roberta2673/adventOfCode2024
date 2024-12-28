import utils as u
import itertools

def add(gr, vet):
    if all([c not in gr for c in itertools.permutations(vet, len(vet))]):
          gr.add(tuple(vet))
 
def getGr(n = 3):
    gr = set()
    for (a,b), (c,d) in itertools.combinations(conn, 2):
        g  = sorted(list(set([a,b,c,d])))
        if len(g) == 3:
                    if all([co in conn for co in itertools.combinations(g,2)]):
                        add(gr, g)
    return gr
 
def main():
    global conn  
    input, st = u.getInput("23", False)     	    	
    conn = []
    for line in input.splitlines():
        conn.append(tuple(sorted((line.split("-")[0], line.split("-")[1]))))
    gr = getGr()
    count = 0
    for g in gr:
        if  g[0].startswith("t") or g[1].startswith("t") or g[2].startswith("t"):
            count += 1
    u.result(count, 1154, st)
    
if __name__ == "__main__":
    exit(main())
