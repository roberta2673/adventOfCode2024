import networkx as nx
import utils as u

def main():
    input, st = u.getInput("23", False)     	    	
    conn = [tuple(sorted((line.split("-")[0], line.split("-")[1]))) for line in input.splitlines()]
    g = nx.Graph(conn)
    max = []
    count = 0
    for s in nx.enumerate_all_cliques(g):
        if (len(s) == 3 and any(x for x in s if x.startswith("t"))):
            count +=1
        if len(s)>len(max):
            max = s
    u.result(count, 1154, st)
    u.result(",".join(sorted(max)), "aj,ds,gg,id,im,jx,kq,nj,ql,qr,ua,yh,zn", st)
        
    
    
if __name__ == "__main__":
    exit(main())
