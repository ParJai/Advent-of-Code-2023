
day = 11
testing = False
f = open(f'inputs/{"samples" if testing else ""}/day{day}.txt').read().splitlines()
f2 = f[:]

def part1():
    line = 0
    while line < len(f):
        if '#' not in f[line]:
            f.insert(line+1, f[line])
            line += 1
        line += 1
    col = 0
    while col < len(f[0]):
        empty = True
        for row in range(len(f)):
            if f[row][col] == '#': empty = False
        if empty:
            for row in range(len(f)):
                f[row] = f[row][:col+1] + '.' + f[row][col+1:]
            col += 1
        col += 1
    galaxies = []
    for r in range(len(f)):
        for c in range(len(f[r])):
            if f[r][c] == '#': galaxies.append((r, c))
    total = 0
    for i in range(len(galaxies)-1):
        for j in range(i+1, len(galaxies)):
            dist = abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
            total += dist
    return total

def part2():
    shift = 1000000
    shift -= 1
    galaxies = []
    for r in range(len(f2)):
        for c in range(len(f2[r])):
            if f2[r][c] == '#': galaxies.append([r, c, 0, 0])
    for line in range(len(f2)):
        if '#' not in f2[line]:
            for g in galaxies:
                if g[0] > line:
                    g[2] += 1
    for col in range(len(f2[0])):
        empty = True
        for row in range(len(f2)):
            if f2[row][col] == '#': empty = False
        if empty:
            for g in galaxies:
                if g[1] > col:
                    g[3] += 1
    for g in galaxies:
        g[0] += (g[2] * shift)
        g[1] += (g[3] * shift)
    total = 0
    for i in range(len(galaxies)-1):
        for j in range(i+1, len(galaxies)):
            dist = abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
            total += dist
    return total

print('Part 1 Answer:', part1())
print('Part 2 Answer:', part2())
