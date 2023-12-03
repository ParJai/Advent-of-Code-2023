
testing = False
f = open(f'inputs/{"samples" if testing else ""}/day3.txt').read().splitlines()

def makeGrid(file):
    grid = []
    for line in file:
        grid.append([])
        for char in line:
            grid[-1].append(char)
    return grid

def getAdjacents(x, y, grid):
    adj = []
    for pos in [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]:
        if 0 <= pos[0] < len(grid[0]) and 0 <= pos[1] < len(grid):
            adj.append(grid[pos[1]][pos[0]])
    return adj

def getAdjacentsPos(x, y, grid):
    adj = []
    for pos in [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]:
        if 0 <= pos[0] < len(grid[0]) and 0 <= pos[1] < len(grid):
            adj.append(pos)
    return adj

def gridPrint(g):
    for row in range(len(g)):
        print(g[row])
        
def getNum(x, y, grid):
    lineSegL = grid[y][:x+1]
    pos = len(lineSegL)-1
    while pos >= 0 and lineSegL[pos].isdigit(): pos -= 1
    left = ''.join(lineSegL[pos+1:])
    leftStart = pos+1
    
    lineSegR = grid[y][x+1:]
    pos = 0
    for char in lineSegR:
        if char.isdigit(): pos += 1
        else: break
    right = ''.join(lineSegR[:pos])
    
    return (left + right, (leftStart, y))

def part1():
    grid = makeGrid(f)
    out = []
    lastStart = -1
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col].isdigit():
                for char in getAdjacents(col, row, grid):
                    if char not in '1234567890.':
                        toAdd, start = getNum(col, row, grid)
                        if lastStart != start[0]:
                            out.append(int(toAdd))
                            lastStart = start[0]
                        break
    return sum(out)

def part2():
    grid = makeGrid(f)
    out = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '*':
                adjPos = getAdjacentsPos(col, row, grid)
                numsAdj = []
                for pos in adjPos:
                    if grid[pos[1]][pos[0]].isdigit():
                        numsAdj.append(getNum(pos[0], pos[1], grid))
                numsAdj = list(set(numsAdj))
                if len(numsAdj) == 2: out.append(int(numsAdj[0][0]) * int(numsAdj[1][0]))
    return sum(out)

print('Part 1 Answer:', part1())
print('Part 2 Answer:', part2())
