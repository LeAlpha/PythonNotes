
# Gogo


class Point:
    def draw(self):
        print(draw)


point = Point()
print(type(point))


# Constructor = init: - Husk self!

class pointtwo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def useTwoPoints(self):
        print(self.x*self.y)


classtwo = pointtwo(7, 6)
classtwo.useTwoPoints()
