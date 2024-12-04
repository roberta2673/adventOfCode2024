import utils as u

def main():
    input, st = u.getInput("01")
    left = sorted([int(line.split()[0]) for line in input])
    right = sorted([int(line.split()[1]) for line in input])
    u.result(sum([max(right[n], left[n]) - min(right[n], left[n]) for n in range(len(left))]), 1319616, st)
    u.result(sum([num * right.count(num) for num in left]), 27267728, st)


if __name__ == "__main__":
    exit(main())
    