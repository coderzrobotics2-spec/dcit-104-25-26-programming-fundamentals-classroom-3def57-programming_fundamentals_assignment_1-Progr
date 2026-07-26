def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row_input = input("Enter row " + str(i + 1) + ": ")
        row_values = row_input.split()

        row = []
        for value in row_values:
            row.append(int(value))

        matrix.append(row)

    return matrix


def print_matrix(matrix):
    for row in matrix:
        line = ""
        for value in row:
            line = line + str(value) + "\t"
        print(line)


def transpose_matrix(matrix, rows, cols):
    result = []

    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(matrix[j][i])
        result.append(new_row)

    return result


def add_matrices(matrix_a, matrix_b, rows, cols):
    result = []

    for i in range(rows):
        new_row = []
        for j in range(cols):
            total = matrix_a[i][j] + matrix_b[i][j]
            new_row.append(total)
        result.append(new_row)

    return result


def multiply_matrices(matrix_a, matrix_b, rows_a, cols_a, cols_b):
    result = []

    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total = total + matrix_a[i][k] * matrix_b[k][j]
            new_row.append(total)
        result.append(new_row)

    return result


print("--- PART A: Transpose a Matrix ---")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = read_matrix(rows, cols)

print()
print("Original Matrix:")
print_matrix(matrix)

transposed = transpose_matrix(matrix, rows, cols)

print()
print("Transposed Matrix:")
print_matrix(transposed)


print()
print("--- PART B: Add Two Matrices ---")
rows = int(input("Enter number of rows for both matrices: "))
cols = int(input("Enter number of columns for both matrices: "))

print("Enter Matrix A:")
matrix_a = read_matrix(rows, cols)

print("Enter Matrix B:")
matrix_b = read_matrix(rows, cols)

sum_matrix = add_matrices(matrix_a, matrix_b, rows, cols)

print()
print("Sum of Matrices:")
print_matrix(sum_matrix)


print()
print("--- PART C: Multiply Two Matrices ---")
rows_a = int(input("Enter number of rows for Matrix A: "))
cols_a = int(input("Enter number of columns for Matrix A (must equal rows of Matrix B): "))

print("Enter Matrix A:")
matrix_a = read_matrix(rows_a, cols_a)

rows_b = cols_a
cols_b = int(input("Enter number of columns for Matrix B: "))

print("Enter Matrix B:")
matrix_b = read_matrix(rows_b, cols_b)

product_matrix = multiply_matrices(matrix_a, matrix_b, rows_a, cols_a, cols_b)

print()
print("Product of Matrices (A x B):")
print_matrix(product_matrix)