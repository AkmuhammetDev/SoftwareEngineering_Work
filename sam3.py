import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

all_sides = one + two + three

min_sides = sorted(all_sides)[:3]
max_sides = sorted(all_sides)[-3:]

def triangle_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    else:
        return None

area_min = triangle_area(min_sides[0], min_sides[1], min_sides[2])
area_max = triangle_area(max_sides[0], max_sides[1], max_sides[2])

print("Площадь треугольника из минимальных сторон:", area_min)
print("Площадь треугольника из максимальных сторон:", area_max)