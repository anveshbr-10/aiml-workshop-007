x= []
print("Enter Square Matrix A: ")
for i in range (3):
    row=[]
    for j in range (3):
        val=int(input(f"X[{i}][{j}]: "))
        row.append(val)
    x.append(row)
    
def is_identity_matrix(x):
    rows = len(x)
    cols = len(x[0])

    # Check if the matrix is square
    if rows != cols:
        return False

    for i in range(rows):
        for j in range(cols):
            if i == j:
                if x[i][j] != 1:
                    return False
            else:
                if x[i][j] != 0:
                    return False
    return True

if is_identity_matrix(x):
    print("The matrix is an identity matrix.")
else:
    print("The matrix is not an identity matrix.")
