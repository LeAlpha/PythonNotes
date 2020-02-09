# For at hente libs, eller klasser:
import math


exampleString = "Whamble"
exampleint = 200


#length : len
print(len(exampleString))


# Find adressen i memory: id()
print(id(exampleString))


# Find index af en del af en streng eksempelvis
print(exampleString.find("amb"))


# Erstat en del med noget andet
print(exampleString)
print(exampleString.replace("a", "o"))


# Findes "input" i string
print(exampleString)
print("Wha" not in exampleString)
print("Wha" in exampleString)


# Print binær/hexa version af nummer
print(bin(exampleint))
print(hex(exampleint))
