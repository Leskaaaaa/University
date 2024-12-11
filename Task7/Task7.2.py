def is_point_inside_circle(x, y, a, b, r):
    distance_squared = (x - a)**2 + (y - b)**2
    return distance_squared < r**2

def count_points_inside_circle(points, a, b, r):
    count = 0
    for x, y in points:
        if is_point_inside_circle(x, y, a, b, r):
            count += 1
    return count

print("Введите параметры окружности (a, b, R):")
a = float(input("a (координата центра по x): "))
b = float(input("b (координата центра по y): "))
r = float(input("R (радиус): "))

print("Введите координаты точек P, F и L (через пробел):")
p1, p2 = map(float, input("P (p1 p2): ").split())
f1, f2 = map(float, input("F (f1 f2): ").split())
l1, l2 = map(float, input("L (l1 l2): ").split())

points = [(p1, p2), (f1, f2), (l1, l2)]

count = count_points_inside_circle(points, a, b, r)

print(f"Количество точек внутри окружности: {count}")