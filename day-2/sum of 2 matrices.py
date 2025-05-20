x = []
y = []
sum = []


print("Enter values for matrix X (3x3):")
for i in range(3):
    row = []
    for j in range(3):
        val = int(input(f"X[{i}][{j}]: "))
        row.append(val)
    x.append(row)


print("Enter values for matrix Y (3x3):")
for i in range(3):
    row = []
    for j in range(3):
        val = int(input(f"Y[{i}][{j}]: "))
        row.append(val)
    y.append(row)


for i in range(3):
    row = []
    for j in range(3):
        row.append(x[i][j] + y[i][j])
    sum.append(row)


print("Sum of matrices:")
for r in sum:
    print(r)