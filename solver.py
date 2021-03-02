import math


def solve(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return str(3)
            else:
                return str(0)
        else:
            return str(1) + "," + str(-c / b)
    else:
        D = b ** 2 - 4 * a * c
        if D < 0:
            return str(0)
        else:
            if D == 0:
                return str(1) + "," + str(-b / (2 * a))
            else:
                return str(2) + "," + str((-b + math.sqrt(D)) / (2 * a)) + "," + str((-b - math.sqrt(D)) / (2 * a))


