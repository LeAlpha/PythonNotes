# En diktionary, som er par af key og value par.
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)

# Find value til key:
print(point["x"])

# tilføj key
point["z"] = 200

# delete
del point["x"]
print(point)

# hent value til key
value = point.get("z")
print(value)

# hvis item ikke findes, tilføj default value:
value = point.get("½", 299)
print(value)


# Iterate over dictionary
for key, value in point.items():
    print(key, value)

print(list(point.items()))


# Kombiner:
dict(zip())


# Comprehensions
