import numpy as np

def Compute(startIndex, list):
    global programRunning
    opcode = list[startIndex]
    index1, index2 = list[startIndex + 1], list[startIndex + 2]
    input1, input2 = list[index1], list[index2]
    outputIndex = list[startIndex + 3]

    if(opcode == 1):
        list[outputIndex] = input1 + input2

    if(opcode == 2):
        list[outputIndex] = input1 * input2

    if(opcode == 99):
        print('Program complete. Value at position 0 is {}'.format(list[0]))
        programRunning = False


inputFile = open("day2input.txt","r")
input = inputFile.read().split(",")
inputFile.close()

for i in range(len(input)):
    input[i] = int(input[i])

input[1], input[2] = 12, 2

programRunning = True
startIndex = 0
while(programRunning):
    Compute(startIndex, input)
    startIndex += 4
