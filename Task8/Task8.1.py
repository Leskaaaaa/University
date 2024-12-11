def find_min_max_sum_rows(matrix):
    min_sum = float('inf')
    max_sum = float('-inf')
    min_row = max_row = None

    for row in matrix:
        row_sum = sum(row)
        if row_sum < min_sum:
            min_sum = row_sum
            min_row = row
        if row_sum > max_sum:
            max_sum = row_sum
            max_row = row

    return min_row, min_sum, max_row, max_sum

print("Введите размеры матрицы (количество строк и столбцов):")
n, m = map(int, input().split())

print("Введите элементы матрицы построчно:")
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

min_row, min_sum, max_row, max_sum = find_min_max_sum_rows(matrix)

print("Строка с минимальной суммой элементов:", min_row, "Сумма:", min_sum)
print("Строка с максимальной суммой элементов:", max_row, "Сумма:", max_sum)