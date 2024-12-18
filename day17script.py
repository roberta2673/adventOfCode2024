import re
import utils as u

def combo(n, regA, regB, regC):
    if n in range(0,4):
        return n
    if n == 4:
        return regA
    if n == 5:
        return regB
    if n == 6:
        return regC

def execute(regA, regB, regC):
    curr = 0
    result = []
    while curr < len(program):
        opcode = program[curr]
        operand = program[curr+1]
        curr += 2
        if opcode == 0:
            regA= int(regA / (2 ** combo(operand, regA, regB, regC)))
        elif opcode == 1:
            regB ^= operand
        elif opcode == 2:
            regB= combo(operand, regA, regB, regC) % 8
        elif opcode == 3:
            if regA != 0:
                curr =  operand
                continue
        elif opcode == 4:
            regB ^= regC
        elif opcode == 5:
            res = combo(operand, regA, regB, regC) % 8
            result += [res]
        elif opcode == 6:
            regB= int(regA / (2 ** combo(operand, regA, regB, regC)))
        elif opcode == 7:
            regC = int(regA / (2 ** combo(operand, regA, regB, regC)))
    return result

def main():
    global program
    input, st = u.getInput("17", False)
    regex = r"Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)\n\nProgram: (.*)"
    matches = re.finditer(regex, input, re.MULTILINE)
    for match in matches:
        regA= int(match.group(1))
        regB= int(match.group(2))
        regC= int(match.group(3))
        program = [int(n) for n in match.group(4).split(",")]
    u.result(execute(regA, regB, regC), [5, 1, 3, 4, 3, 7, 2, 1, 7], st)
    
    todo = [(1, 0)]
    candidates = []
    for i, a in todo:
        for a in range(a, a+8):
            if execute(a, 0, 0) == program[-i:]:
                todo += [(i+1, a*8)]
                if i == len(program): 
                    candidates.append(a)
    u.result(candidates[0], 216584205979245, st)
                
if __name__ == "__main__":
    exit(main())
