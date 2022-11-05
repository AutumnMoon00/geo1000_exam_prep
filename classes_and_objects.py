import math
import copy


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

# 15.1
class Circle:
    """
    attributes: center, radius
    """


def point_in_circle(c, p):
    if distance_between_points(c.center, p) <= c.radius:
        return True
    else:
        return False

def find_center(box):
    center = Point()
    center.x = box.corner.x + box.width/2
    center.y = box.corner.y + box.height/2
    return center


def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight


def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy


def move_rectangle_copy(rect, dx, dy):
    rect_copy = copy.deepcopy(rect)
    move_rectangle(rect_copy, dx, dy)
    return rect_copy


def main():
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

    print(box.width, box.height)
    grow_rectangle(box, 50, 100)
    print(box.width, box.height)

    p1 = Point()
    p1.x = 3.0
    p1.y = 4.0

    p2 = copy.deepcopy(p1)
    print(p2 == p1)


if __name__ == '__main__':
    main()