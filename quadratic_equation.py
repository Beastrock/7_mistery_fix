from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    # можем смело посчитать корни, тк тут уже случаи с d>0
    root1 = (-b - sqrt(discriminant)) / (2 * a)
    root2 = (-b + sqrt(discriminant)) / (2 * a)
    if discriminant > 0:
        return root1, root2
    elif discriminant == 0:
        return root1, None
