class Point:
    """
    Represents a point in a 2D space
    """


blank = Point()
blank.x = 3.0
blank.y = 4.0


def print_point(point):
    print("(%g, %g)" %(point.x, point.y))


print_point(blank)
