def transform_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < 0:
                matrix[i][j] = 0
            else:
                matrix[i][j] = 1
    return matrix

def print_lower_triangle(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1):
            print(matrix[i][j], end=" ")
        print()

print("Введите размер матрицы N (N x N):")
n = int(input())

print("Введите элементы матрицы построчно:")
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

transformed_matrix = transform_matrix(matrix)

print("Нижняя треугольная матрица:")
print_lower_triangle(transformed_matrix)