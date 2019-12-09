from copy import deepcopy

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
    currentVisitedCoords = []

    wire = wires[number].split(",")
    for instruction in wire:
        FollowInstruction(instruction)

    currentVisitedCoords.sort(key = lambda c: c.x + c.y)

    visitedCoords.append(deepcopy(currentVisitedCoords))
    currentCoords = Coord(0, 0)
    currentVisitedCoords = []

def FindClosestIntersect():
    global visitedCoords
    wireDistance = 0
    for coord0 in visitedCoords[0]:
        wireDistance = coord0.x + coord0.y
        for coord1 in visitedCoords[1]:
            if (coord1.x + coord1.y == wireDistance):
                if coord0.x == coord1.x and coord0.y == coord1.y:
                    return coord0.x, coord0.y, coord0.x + coord0.y
# main

inputFile = open("day3input.txt","r")
wires = inputFile.read().split("\n")
inputFile.close()

currentCoords = Coord(0, 0)
visitedCoords = []
currentVisitedCoords = []
intersectFound = False

LogAllCoords(0)
LogAllCoords(1)

print FindClosestIntersect()