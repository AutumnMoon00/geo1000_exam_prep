class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        text = '(%g, %g)' % (self.x, self.y)


    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.add_tuple(other)

    def add_point(self, other):
        return Point(self.x + other.x, self.y + other.yself.y + other.y)

    def add_tuple(self, other):
        return Point(self.x + other[0], self.y + other[1])

