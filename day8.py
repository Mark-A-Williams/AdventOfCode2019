def CountNumbers(index):
    global input

    startPixel = numPixels * index
    layer = input[startPixel: startPixel + numPixels]
    return layer.count("0"), layer.count("1"), layer.count("2")

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