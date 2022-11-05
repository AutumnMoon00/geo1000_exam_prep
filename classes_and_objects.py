import math


class Point:
    """
    Represents a point in a 2D space
    """


def distance_between_points(pt1, pt2):
    dx = pt2.x - pt1.x
    dy = pt2.y - pt1.y
    dist = math.sqrt(dx**2 + dy**2)
    return dist


def print_point(point):
    print("(%g, %g)" %(point.x, point.y))


class Rectangle:
    """
    attributes: width, height, corner
    """


def find_center(box):
    center = Point()
    center.x = box.corner.x + box.width/2
    center.y = box.corner.y + box.height/2
    return center


box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0


blank = Point()
blank.x = 3.0
blank.y = 4.0


center = find_center(box)
print_point(center)
