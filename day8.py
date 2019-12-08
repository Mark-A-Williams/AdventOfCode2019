def CountNumbers(index):
    global input

    startPixel = numPixels * index
    layer = input[startPixel: startPixel + numPixels]
    return layer.count("0"), layer.count("1"), layer.count("2")

def FindPixelColour(pixel):
    global input, numLayers

    for i in range(numLayers):
        pixelValue = int(input[numPixels * i + pixel])
        if (pixelValue != 2):
            return pixelValue
    return 2

# main

inputFile = open("day8input.txt", "r")
input = inputFile.read().rstrip()
inputFile.close()

numPixels = 25 * 6
numLayers = len(input)/numPixels
layerWithFewestZeros = 0
zerosInLayer = 150

for i in range(numLayers):
    zeros, ones, twos = CountNumbers(i)
    if zeros < zerosInLayer:
        layerWithFewestZeros = i
        zerosInLayer = zeros

print layerWithFewestZeros
zeros, ones, twos = CountNumbers(layerWithFewestZeros)
print ones * twos

# part 2

image = [2] * numPixels

for i in range(len(image)):
    image[i] = FindPixelColour(i)

for i in range(6):
    print image[ 25*i : 25*(i+1) ]

# then employee the very sophisticated method of "squint a bit and try and make out words"
