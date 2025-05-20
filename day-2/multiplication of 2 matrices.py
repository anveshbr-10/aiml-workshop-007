x = []

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
if rows != columns:
    raise ValueError("Matrix must be square to compute diagonal sum")
# Input for matrix x
print("Enter values for matrix X:")
for i in range(rows):
    row = []
    for j in range(columns):
        val = int(input(f"X[{i}][{j}]: "))
        row.append(val)
    x.append(row)

y = []
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
if rows != columns:
    raise ValueError("Matrix must be square to compute diagonal sum")
# Input for matrix y
print("Enter values for matrix Y:")
for i in range(rows):
    row = []
    for j in range(columns):
        val = int(input(f"Y[{i}][{j}]: "))
        row.append(val)
    y.append(row)

# Result matrix (initialized with zeros)
result = [[0 for _ in range(len(y[0]))] for _ in range(len(x))]

# Matrix multiplication logic
for i in range(len(x)):          
    for j in range(len(y[0])):    
        for k in range(len(y)):  
            result[i][j] += x[i][k] * y[k][j]

# Output the result
for row in result:
    print(row)
