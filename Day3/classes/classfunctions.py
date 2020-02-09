class Point:
    def draw(self):
        print("Nosing")


point = Point()
point.draw()


# Tjek for om et enkelt object tilhøre en bestemt klasse
print(isinstance(point, Point))


# Definer en instance, i klassen, som kan oprettes med default values:

class person:
    def __init__(self, name, phonenumber):
        self.name = name
        self.phonenumber = phonenumber

    # @ er en decorater - cls er bare en variabel
    @classmethod
    def johnDoe(cls):
        return person("johnDohe", 1235)

    def printDefault(self):
        print(self.name)


randomPerson = person.johnDoe()
randomPerson.printDefault()
