# Sorter:
numbers = [512, 2321, 33, 11, 3, 4, 5, 76]
numbers.sort()
print(numbers)


# Sorter baglæns
numbers = [512, 2321, 33, 11, 3, 4, 5, 76]
numbers.sort(reverse=True)
print(numbers)


# Nemmere måde:
numbers = [512, 2321, 33, 11, 3, 4, 5, 76]
print(numbers)
print(sorted(numbers))
print(sorted(numbers, reverse=True))


# Sorting tuples:
items = [
    ("productOne", 30),
    ("productTwo", 400),
    ("productThree", 2),
]


def sortItem(item):
    return item[1]


items.sort(key=sortItem)
print(items)


# Dette kan gøres med en engangs function (lambda funktion)
items = [
    ("productOne", 30),
    ("productTwo", 400),
    ("productThree", 2),
]

items.sort(key=lambda items: items[1])
print(items)
