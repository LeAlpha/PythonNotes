
liste = [1, 2, 3]

# For over liste
for i in liste:
    print(i)


# For loop til at finde noget i string:
listTwo = ["Juan", "Two", "Three", "Flour", "Fivo", ]
counter = 0
for i in listTwo:
    if i.startswith("F"):
        counter += 1
print("Found ", counter, "in list that starts with \"F\" \n")


# For loop kan have else clauses:

listThree = ["Juan", "Two", "Three", "Flour", "Fivo", ]
for i in listTwo:
    if i.startswith("8"):
        print("Found")

else:
    print("nothing")


# While

startCon = 0
stopCon = 10
while stopCon != startCon:
    startCon += 1
    print(startCon)
else:
    print("reached")
