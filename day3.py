from copy import deepcopy
import math

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def Right(self):
        self.x += 1
    def Left(self):
        self.x -= 1
    def Up(self):
        self.y += 1
    def Down(self):
        self.y -= 1
    def Distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

def InterpretDirections(raw):
    direction = raw[0]
    distance = raw[1:]
    return direction, int(distance)

def FollowInstruction(raw):
    global currentCoords, currentVisitedCoords

    direction, distance = InterpretDirections(raw)

    for i in range(distance):
        if(direction == 'R'):
            currentCoords.Right()
        if(direction == 'L'):
            currentCoords.Left()
        if(direction == 'U'):
            currentCoords.Up()
        if(direction == 'D'):
            currentCoords.Down()
        currentVisitedCoords.append(deepcopy(currentCoords))

def LogAllCoords(number):
    global currentCoords, currentVisitedCoords

    wire = wires[number].split(",")
    for instruction in wire:
        FollowInstruction(instruction)
    
    visitedCoords.append(deepcopy(currentVisitedCoords))
    currentCoords = Coord(0, 0)
    currentVisitedCoords = []

# main

inputFile = open("day3input.txt","r")
wires = inputFile.read().split("\n")
inputFile.close()

currentCoords = Coord(0, 0)
visitedCoords = []
currentVisitedCoords = []

LogAllCoords(0)
LogAllCoords(1)

print 'done'

# for coords in visitedCoords:
#     print coords.x, coords.y
