def transform_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < 0:
                matrix[i][j] = 0
            else:
                matrix[i][j] = 1
    return matrix

def print_lower_triangle(matrix, output_file):
    n = len(matrix)
    with open(output_file, "w") as f:
        for i in range(n):
            for j in range(i + 1):
                f.write(f"{matrix[i][j]} ")
            f.write("\n")

def read_matrix_from_file(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()
        n = int(lines[0].strip())
        matrix = [list(map(int, lines[i + 1].split())) for i in range(n)]
    return matrix

input_file = "РвачевАС_Ум-242_vvod.txt"
output_file = "РвачевАС_Ум-242_vivod.txt"

matrix = read_matrix_from_file(input_file)

transformed_matrix = transform_matrix(matrix)

print_lower_triangle(transformed_matrix, output_file)
