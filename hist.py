def histogram(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    return d


class Jumble:
    def __init__(self, x=5, y=5):
        self.diff = x - y
        self.sum = x + y


t = ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam']
# print(histogram(t))

j = Jumble(5)
jattr = vars(j)
print(vars(j))


def print_attributes(obj):
    for i in vars(obj):
        print(i, getattr(obj, i))


print_attributes(j)

l1 = ['sharath', 'meghana']
# print(l1)
# print(vars(l1))

