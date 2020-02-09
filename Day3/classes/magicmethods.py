# Standard metoder er magic methods:
# Magic methods er defineret af double underscore: __init__
# Doc: https://rszalski.github.io/magicmethods/#representations


class pointtwo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Man kan også self definere hvad en magic method skal gøre, hvis den kaldes, for en given klasse
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return self.x+other.x, self.y+other.y


point = pointtwo(6, 5)
secondpoint = pointtwo(6, 5)
print(point == secondpoint)
print(point + secondpoint)  # eller:
combined = point+secondpoint
print(combined)
