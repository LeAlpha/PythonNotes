items = [
    ("productOne", 30),
    ("productTwo", 400),
    ("productThree", 2),
]

# Vi vil gerne have numrene ud i en liste for sig. Brug Map funktionen
x = map(lambda item: item[1], items)
# Den returner en adresse til det array, så for at printe, brug for loop:

for items in x:
    print(items)


# Eller

items = [
    ("productOne", 30),
    ("productTwo", 400),
    ("productThree", 2),
]

prices = list(map(lambda item: item[1], items))
print(prices)


# Endnu pænere: Comprehensions
items = [
    ("productOne", 22),
    ("productTwo", 40),
    ("productThree", 265),
]

pricesThree = list([item[1] for item in items])
print(pricesThree)
