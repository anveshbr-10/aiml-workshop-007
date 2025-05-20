rows = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))

matrix = []
for i in range(rows):
    row = []

    for j in range(column):

        val = int(input(f"X[{i}][{j}]: "))

        row.append(val)
    matrix.append(row)

print("The matrix is:")

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed

result = transpose_matrix(matrix)

print("Original matrix:")
for row in matrix:
    print(row)

print("\nTransposed matrix:")
for row in result:
    print(row)
