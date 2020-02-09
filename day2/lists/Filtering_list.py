items = [
    ("productOne", 30),
    ("productTwo", 400),
    ("productThree", 2),
]

# Her kan vi bruge filter function, til at hente en liste med udelukkende det vi gerne vil have
filtered_prices = list(filter(lambda item: item[1] >= 10, items))
print(filtered_prices)


# Endnu pænere ved comprehension
filteredTwo = [item for item in items if item[1] <= 2]
print(filteredTwo)
