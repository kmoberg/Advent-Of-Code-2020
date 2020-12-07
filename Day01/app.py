# Advent of Code
# Karl Mathias Moberg
# Day 1
import itertools

def compareNumbers(num1, num2, num3 = 0):
    
    numSum = num1 + num2 + num3

    if numSum == 2020:
        if num3 == 0:
            matchSum = num1 * num2

            print("MATCH: {} + {} = 2020. Multiplier: {}".format(num1, num2, matchSum))
        elif num3 > 0:
            
            matchSum = (num1 * num2 * num3)
            print("MATCH: {} + {} + {} = 2020. Multiplier: {}".format(num1, num2, num3, matchSum))
        

inputFile = "input.txt"

with open(inputFile) as f:
    numbers = f.read().splitlines()

for a,b in itertools.combinations(numbers, 2):
    compareNumbers(int(a),int(b))

for a,b,c in itertools.combinations(numbers, 3):
    compareNumbers(int(a),int(b), int(c))
