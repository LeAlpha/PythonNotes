Age = 27

# Vi bruger ikke parantes, eller turborgklammer. Brug komma, og tabs


# if, else og else if
# brug pass, til ikke at gøre noget

if Age > 27:
    print("Adulting")
elif Age == 27:
    print("just right")
else:
    print("NotSoAdulting")
    pass


# Eller på en anden måde :

alder = "VoksenAF" if Age >= 26 else "BabyAF"
print(alder)
