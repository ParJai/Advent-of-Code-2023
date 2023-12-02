
f = open('inputs/day1.txt').read().splitlines()

def part1():
    sum = 0
    for line in f:
        num = ''
        for char in line:
            if char in '1234567890': num += char
        sum += 10*int(num[0]) + int(num[-1])
    return sum

def part2():
    sum = 0
    for line in f:
        num = ''
        for char in range(len(line)):
            if line[char] in '1234567890': num += line[char]
            for digit in ['one1', 'two2', 'three3', 'four4', 'five5', 'six6', 'seven7', 'eight8', 'nine9']:
                if line[char:(char+len(digit)-1)] == digit[:-1]: num += digit[-1]
        sum += 10*int(num[0]) + int(num[-1])
    return sum

print('Part 1 Answer:', part1())
print('Part 2 Answer:', part2())
