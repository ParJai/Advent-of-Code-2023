
day = 9
testing = False
f = open(f'inputs/{"samples" if testing else ""}/day{day}.txt').read().splitlines()

def part1():
    total = 0
    for line in f:
        diffs = [[int(x) for x in line.split()]]
        quit = False
        while not quit:
            zeroed = True
            diffs.append([])
            for i in range(len(diffs[-2])-1):
                num1, num2 = diffs[-2][i], diffs[-2][i+1]
                d = num2 - num1
                diffs[-1].append(d)
                if d != 0: zeroed = False
            if zeroed:
                quit = True
        for seq in range(len(diffs)-1, 0, -1):
            add1, add2 = diffs[seq][-1], diffs[seq-1][-1]
            diffs[seq-1].append(add1+add2)
        next = diffs[0][-1]
        total += next
    return total

def part2():
    total = 0
    for line in f:
        diffs = [[int(x) for x in line.split()]]
        quit = False
        while not quit:
            zeroed = True
            diffs.append([])
            for i in range(len(diffs[-2])-1):
                num1, num2 = diffs[-2][i], diffs[-2][i+1]
                d = num2 - num1
                diffs[-1].append(d)
                if d != 0: zeroed = False
            if zeroed:
                quit = True
        for seq in range(len(diffs)-1, 0, -1):
            add1, add2 = diffs[seq][0], diffs[seq-1][0]
            diffs[seq-1].insert(0, add2-add1)
        next = diffs[0][0]
        total += next
    return total

print('Part 1 Answer:', part1())
print('Part 2 Answer:', part2())
