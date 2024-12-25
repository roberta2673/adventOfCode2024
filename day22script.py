from itertools import combinations
from math import floor
import utils as u
import table as t
import heapq

def mix (secret, n):
    return secret ^ n

def prune(secret):
    return secret % 16777216

def process(secret):
    secret = prune(mix(secret, secret*64))
    secret = prune(mix(secret, floor(secret/32)))
    secret = prune(mix(secret, secret*2048))
    return secret

def price(n):
    return int(str(n)[-1])

def main():
    global table
    input, st = u.getInput("22") 
    sum = 0
    results = [[]]*len(input)
    maxPrices = [[0]]*len(input)
    print(maxPrices)
    for i, n in enumerate(input):
        n = n.removesuffix("\n")
        res = n
        results[i].append((price(n), price(n)))
        for iter in range(2000):
            res = process(int(res))
            pr = price(res)
            if [diff for _, diff in results[i][-4:]] == [-2, 1, -1, 3]:
                print(i, pr)
            if pr > maxPrices[i][0]:
                maxPrices[i] = ((pr, [diff for _, diff in results[i][-4:]]))
            results[i].append((pr, pr-results[i][-1][0]))
        sum += res
    print(sum)
    print(maxPrices)
    
if __name__ == "__main__":
    exit(main())
