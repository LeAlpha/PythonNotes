

class Point:
    default_farve = "rød"

    def draw(self):
        print(self.default_farve)


point = Point()
print(type(point))
point.draw()


# Constructor = init: - Husk self!


class pointtwo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def useTwoPoints(self):
        print(self.x*self.y)


classtwo = pointtwo(7, 6)
classtwo.useTwoPoints()

# Class values er delt af alle instances.
# Der kan derfor ændres i alle instances, ved at ændre class level attributes ( se default farve )
Point.default_farve = "NotSoRoet"
print(point.default_farve)


# Man kan tilføje variabler efter at en class er lavet:
classtwo.p = "SeeDisShiet?"
print(classtwo.p)
