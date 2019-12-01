import numpy as np

def FuelRequired(mass):
    fuel = np.floor(mass/3)-2
    return (fuel + FuelRequired(fuel) if fuel > 0 else 0)

inputFile = open("day1input.txt","r")
input = inputFile.readlines()
inputFile.close()

fuelMass = 0
payloadMass = 0

for line in input:
    moduleMass = int(line.rstrip())
    payloadMass += moduleMass
    fuelMass += FuelRequired(moduleMass)

print fuelMass

specificImpulse = 243 # equal to that of a Saturn V first stage
deltaV = 9.81 * specificImpulse * np.log((fuelMass + payloadMass) / payloadMass)
print deltaV

# Delta-v comes to just under 1000 m/s. For comparison, around 9400 m/s is needed just to reach Earth orbit.
