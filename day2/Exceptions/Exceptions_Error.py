# out of bounds:
numbers = [1, 2, 3]
try:
    print(numbers[1])
except:
    print("Out of bounds i error message")
else:
    print("execution worked")

# value error exception:

try:
    age = int(input("Indtast Int"))
except ValueError as ex:
    print("Exception reached: Value error")
else:
    print("execution worked")


# Tilføj flere exceptions:

try:
    age = int(input("Indtast Int"))
    divisionMedNul = 1/age
except (ValueError, ZeroDivisionError):
    print("Exception reached: Value error, eller division med 0")
else:
    print("execution worked")


# In case at eksempelvis en fil skal lukkes, men kunne rammes af en exception på vejen, da bruges finally:
try:
    file = open("testfile.txt")
except ValueError:
    print("Exception that does not get reached")
finally:
    file.close


# Ved brug af hvisse funktioner såsom "open" kan man bruge "with" som selv sørger for at lukke ned. Derfor kan man
# skrotte finally


try:
    with open("testfile.txt") as file:
        print("do stuff")
except ValueError:
    print("Exception that does not get reached")


# Hvis flere ressourcer:
try:
    with open("testfile.txt") as readfile, open("testfile2.txt") as targetfile:
        print("do stuff")
except ValueError:
    print("Exception that does not get reached")


# Lav egen via raise :

def calculate(age):
    if age <= 0:
        raise ValueError("Her kan egen exception skrives")
    return age / 10
