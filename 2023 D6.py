
day = 6
testing = False
f = open(f'inputs/{"samples" if testing else ""}/day{day}.txt').read().splitlines()

def part1():
    margin = 1
    times = [int(x) for x in f[0].split(':')[1].split()]
    records = [int(x) for x in f[1].split(':')[1].split()]
    for race in range(len(times)):
        canWin = 0
        for i in range(times[race]+1):
            if i*(times[race]-i) > records[race]: canWin += 1
        margin *= canWin
    return margin

def part2():
    canWin = 0
    time = int(''.join(f[0].split(':')[1].split()))
    record = int(''.join(f[1].split(':')[1].split()))
    for i in range(time+1):
        if i*(time-i) > record: canWin += 1
    return canWin

print('Part 1 Answer:', part1())
print('Part 2 Answer:', part2())
