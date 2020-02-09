# Functioner defineres på følgende måde:


def increment(nummer, hvormeget):
    return nummer + hvormeget


print(increment(2, 2))

# Der kan returnes mere end én ting.


def incrementTwo(nummer, hvormeget):
    return (nummer, nummer+hvormeget)


print(incrementTwo(4, 4))
# Her hentes touple return
x, y = incrementTwo(4, 4)

print(x, y)


# Tilføj typer til funktionen, og til return:

def incrementthree(nummer: int, hvormeget: int) -> tuple:
    return (nummer, nummer+hvormeget)


x, y = incrementthree(8, 16)
print(x, y)

# Når vi så prøver at ændre til noget andet:
x, y = incrementthree("lol", "getRekt")


# Hvis vi vil lave en funktion som tager en tilfældig størelse ind -
# Smid en * ind så det bliver en tuple
numberlist = [1, 2, 3, 5, 6]


def multiplilist(*list):
    total = 1
    for nummer in list:
        total *= nummer
    return total


print(multiplilist(2, 3, 4, 5))
