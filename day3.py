from copy import deepcopy
import math
import time

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
    currentVisitedCoords = []

    wire = wires[number].split(",")
    for instruction in wire:
        FollowInstruction(instruction)
    
    visitedCoords.append(deepcopy(currentVisitedCoords))
    currentCoords = Coord(0, 0)
    currentVisitedCoords = []

def CheckOnRoute(x, y, number):
    return any((elem.x == x and elem.y == y) for elem in visitedCoords[number])

def CheckIntersect(x, y):
    global intersectFound
    if (CheckOnRoute(x, y, 0) and CheckOnRoute(x, y, 1)):
        print "Intersect found: ({}, {})".format(x, y)
        intersectFound = True
    # else:
    #     print "Checked coords ({}, {})".format(x, y)

def LookForIntersectsInSquare(radius):
    global lookingForIntersects, intersectFound
    print 'checking square with radius {}'.format(radius)
    x, y = 0 - radius, 0
    while (x < 0 ):
        CheckIntersect(x, y)
        x += 1
        y += 1
    while (y > 0):
        CheckIntersect(x, y)
        x += 1
        y -= 1
    while (x > 0):
        CheckIntersect(x, y)
        x -= 1
        y -= 1
    while (y < 0):
        CheckIntersect(x, y)
        x -= 1
        y += 1


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

print 'done'

start = time.time()
lookingForIntersects = True
radius = 1
while (lookingForIntersects):
    LookForIntersectsInSquare(radius)
    radius += 1
end = time.time()
print end-start

# for coord in visitedCoords[0]:
#     if (any((elem.x == coord.x & elem.y == coord.y) for elem in visitedCoords[1])):
#         print "Duplicate coordinate: ({}, {})".format(coord.x, coord.y)


# you might think this would work

# x, y = 9123, 7
# if (any(elem.x == x & elem.y == y) for elem in visitedCoords[0]):
#     print "Duplicate coordinate: ({}, {})".format(x, y)
# ok why the hell does this not evaluate to true. it works with 10,0 but not anything much larger.


# for i in range(100):
#     print visitedCoords[0][i].x, visitedCoords[0][i].y

# x, y = 9122, 7
# result = any((elem.x == x & elem.y == y) for elem in visitedCoords[0])
# if result:
#     print 'correct'

# for coords in visitedCoords:
#     print coords.x, coords.y