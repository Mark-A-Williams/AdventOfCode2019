import numpy as np

def Compute(startIndex, list):
    if(startIndex >= len(list)):
        print 'problem1'
        return False, list

    opcode = list[startIndex]    
    index1, index2 = list[startIndex + 1], list[startIndex + 2]
    input1, input2 = list[index1], list[index2]
    outputIndex = list[startIndex + 3]

    if(opcode == 1):
        list[outputIndex] = input1 + input2
        return True, list

    if(opcode == 2):
        list[outputIndex] = input1 * input2
        return True, list

    if(opcode == 99):
        return False, list

    else:
        print 'problem2'
        print opcode
        return False, list

def IntcodeComputer(param1, param2, list):
    list[1], list[2] = param1, param2

    programRunning = True
    startIndex = 0
    while(programRunning):
        programRunning, list = Compute(startIndex, list)
        startIndex += 4

    return list[0]

def FindInputs(desiredResult, acceptableRange):
    global input
    for i in range(acceptableRange):
        for j in range(acceptableRange):
            list = input[:]
            result = IntcodeComputer(i, j, list)
            if(result == desiredResult):
                return i, j

# Main

inputFile = open("day2input.txt","r")
input = inputFile.read().split(",")
inputFile.close()

for i in range(len(input)):
    input[i] = int(input[i])

noun, verb = FindInputs(19690720, len(input))

print 100 * noun + verb