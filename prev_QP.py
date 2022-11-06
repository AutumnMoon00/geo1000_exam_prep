def score(x):
    lut = {"A*": 6, "A": 5, "B": 4, "C": 3, "D": 2, "E": 1}
    return lut[x]

grades = [("Adam", "A"),
        ("Brian", "B"),
        ("Ramona", "C"),
        ("Kimberly", "E"),
        ("Charles", "A*")]
D = []
for student in grades:
    D.append( (len(student[0]), student) )
D.sort()
U = []
for d in D:
    U.append(d[1])
U.reverse()
print(U)
