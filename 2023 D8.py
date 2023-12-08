import math

day = 8
testing = False
f = open(f'inputs/{"samples" if testing else ""}/day{day}.txt').read().splitlines()

def part1():
    instructions = f[0]
    mod = len(instructions)
    nodes = {}
    for line in f[2:]:
        nodes[line[0:3]] = [line[7:10], line[12:15]]
    steps = 0
    current = 'AAA'
    i = 0
    while current != 'ZZZ':
        if instructions[i] == 'L':
            current = nodes[current][0]
        else:
            current = nodes[current][1]
        steps += 1
        i = (i+1) % mod
    return steps

def part2():
    instructions = f[0]
    mod = len(instructions)
    nodes = {}
    for line in f[2:]:
        nodes[line[0:3]] = [line[7:10], line[12:15]]
    steps = 0
    currents = []
    for n in nodes.keys():
        if n[-1] == 'A': currents.append(n)
    i = 0
    while True:
        if instructions[i] == 'L': dir = 0
        else: dir = 1
        steps += 1
        print(steps)
        j = 0
        for cur in range(len(currents)):
            currents[cur] = nodes[currents[cur]][dir]
            if currents[cur][-1] == 'Z': j += 1
        if len(currents) == j: return steps
        i = (i+1) % mod

def compute_lcm(l):
    least = 1
    for i in range(len(l)):
        least = math.lcm(least, l[i])
    return least

def part2_attempt2():
    instructions = f[0]
    mod = len(instructions)
    
    nodes = {}
    for line in f[2:]:
        nodes[line[0:3]] = [line[7:10], line[12:15]]
        
    steps = 0
    currents = {}
    ZSteps, cycleSteps = -1, -1
    for n in nodes.keys():
        if n[-1] == 'A': currents[n] = [n, ZSteps, cycleSteps]
        
    i = 0
    while True:
        if instructions[i] == 'L': dir = 0
        else: dir = 1
        
        steps += 1

        done = True

        for node in currents.keys():
            next = nodes[currents[node][0]][dir]
            currents[node][0] = next
            if currents[node][0][-1] == 'Z' and currents[node][1] == -1:
                currents[node][1] = steps
            if next in currents[node][0] and currents[node][2] == -1:
                currents[node][2] = steps
            if -1 in currents[node]: done = False
        if done: break
        
        i = (i+1) % mod
    
    return compute_lcm([currents[n][1] for n in currents.keys()])

print('Part 1 Answer:', part1())
print('Part 2 Answer:', part2_attempt2())
