# Tuples er read only, og kan ikke modificeres efter de er lavet
# Touples er defineret som en liste, med () i stedet for []
# Tuples bruges til at sikre at ting ikke bliver ændret.

point = 1, 2
print(type(point))

# Concat 2 touples:

point2 = (1, 2) + (3, 4)
print(point2)


# Konverter liste til touple
liste = [1, 3, 6, 8]
point3 = tuple(liste)
print(point3)
