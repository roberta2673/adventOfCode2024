import utils as u

def sort(numbers):
    for a, b in constraints:
        if a in numbers and b in numbers and numbers.index(a)>numbers.index(b):
            numbers[numbers.index(a)] = b
            numbers[numbers.index(b)] = a
            return False
    return True

def main():
    global constraints
    input, st = u.getInput("05", False)
    constraints = [(o.split("|")[0], o.split("|")[1]) for o in input.split("\n\n")[0].splitlines() ]
    sequences = input.split("\n\n")[1].splitlines()
    sumCorrect, sumIncorrect = 0, 0
    for seq in sequences:
        numbers = seq.split(",")
        if sort(numbers): 
            sumCorrect += (int)(numbers[(int)((len(numbers)-1)/2)]) 
        else:
            while not sort(numbers):
                pass
            sumIncorrect += (int)(numbers[(int)((len(numbers)-1)/2)]) 
    u.result(sumCorrect, 5651, st)
    u.result(sumIncorrect, 4743, st)
    
if __name__ == "__main__":
    exit(main())
