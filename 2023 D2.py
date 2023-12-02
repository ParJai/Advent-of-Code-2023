
f = open('inputs/day2.txt').read().splitlines()

def part1():
    sum = 0
    maxCubes = {'red': 12, 'green': 13, 'blue': 14}
    for line in f:
        valid = True
        gameID = int(line.split(': ')[0].split(' ')[-1])
        cubes = [s.split(', ') for s in line.split(': ')[1].split('; ')]
        cubes = [x for subarray in cubes for x in subarray]
        for c in cubes:
            if int(c.split(' ')[0]) > maxCubes[c.split(' ')[1]]:
                valid = False
        if valid: sum += gameID
    return sum

def part2():
    sum = 0
    for line in f:
        maxCubes = {'red': 0, 'green': 0, 'blue': 0}
        gameID = int(line.split(': ')[0].split(' ')[-1])
        cubes = [s.split(', ') for s in line.split(': ')[1].split('; ')]
        cubes = [x for subarray in cubes for x in subarray]
        for c in cubes:
            if int(c.split(' ')[0]) > maxCubes[c.split(' ')[1]]:
                maxCubes[c.split(' ')[1]] = int(c.split(' ')[0])
        sum += maxCubes['red'] * maxCubes['green'] * maxCubes['blue']
    return sum

print('Part 1 Answer:', part1())
print('Part 2 Answer:', part2())
