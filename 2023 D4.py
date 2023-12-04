
testing = False
f = open(f'inputs/{"samples" if testing else ""}/day4.txt').read().splitlines()

def part1():
    sum = 0
    for line in f:
        exp = 0
        winningNums = line.split(' | ')[0].split(': ')[1].split()
        myNums = line.split(' | ')[1].split()
        for num in myNums:
            if num in winningNums: exp += 1
        sum += (0 if exp == 0 else 2**(exp-1))
    return sum

def part2():
    mults = [1 for i in range(len(f))]
    for line in f:
        won = 1
        winningNums = line.split(' | ')[0].split(': ')[1].split()
        myNums = line.split(' | ')[1].split()
        game = int(line.split(':')[0].split('Card ')[1])-1
        for num in myNums:
            if num in winningNums:
                won += 1
        for i in range(game+1, game+won):
            mults[i] += mults[game]
    return sum(mults)

print('Part 1 Answer:', part1())
print('Part 2 Answer:', part2())
