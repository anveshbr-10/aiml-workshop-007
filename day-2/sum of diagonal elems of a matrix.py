rows = int(input("Enter number of rows: "))

cols = int(input("Enter number of columns: "))
if rows != cols:
    raise ValueError("Matrix must be square to compute diagonal sum")

matrix = []

print("Enter the matrix A: ")
for i in range (rows):
    row = []
    for j in range (cols):
        val=int(input(f"X[{i}][{j}]: "))
        row.append(val)
    matrix.append(row)

def diagonal_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])


    total = 0
    for i in range(rows):
        total += matrix[i][i]
    
    return total

print("Sum of main diagonal elements:", diagonal_sum(matrix))
