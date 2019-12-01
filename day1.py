import numpy as np

def FuelRequired(mass):
    return np.floor(mass/3)-2

inputFile = open("day1input.txt","r")
input = inputFile.readlines()
inputFile.close()

result = 0

for line in input:
    moduleMass = int(line.rstrip())
    result += FuelRequired(moduleMass)

print result
