# Sets er lister uden douplicates
# De er ikke indexeret
# Hvis man selv vil definere bruges kurlybois
numbers = [1, 1, 2, 3, 4, 65, 7]
numberstwo = {2, 3, 5, 6}
theSet = set(numbers)
print(numbers)
print(theSet)
print(numberstwo)

# Funktioner
numberstwo.add(9)


# kombiner 2 sæts via |
print(theSet | numberstwo)
print(sorted(theSet | numberstwo))

# Find dobbeltgængere i to sæt (and)
print(theSet & numberstwo)

# Find forskelle (or)
print(theSet - numberstwo)

# Find dem som er unikke (xor)
print(theSet ^ numberstwo)


# Find instance i sæt:
if 1 in numbers:
    print("findes")
