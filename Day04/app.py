# Advent of Code
# Karl Mathias Moberg
# Day 4

validFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
count = 0

inputFile = "input.txt"

with open(inputFile) as f:
    inputResult = f.read().split('\n\n')

for x in inputResult:
    check = [v in x for v in validFields]
    if all(check):
        count += 1

print(count)