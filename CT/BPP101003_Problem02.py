# Matrix 1
rows1 = int((input("Enter the number of rows of the matrix1: ")))
cols1 = int((input("Enter the number of columns of the matrix1: ")))

matrix1 = [[0 for _ in range(cols1)] for _ in range(rows1)]

print("\n Enter the elements of matrix1")
for i in range (rows1):
    for j in range (cols1):
        matrix1[i][j]= int((input(f"Enter element [{i}][{j}] of matrix1: ")))
        
for r in matrix1:
    print (r)
    
# Matrix 2
rows2 = int((input("Enter the number of rows of the matrix2: ")))
cols2 = int((input("Enter the number of columns of the matrix2: ")))

if cols1 != rows2:
    print("\nMatrix multiplication not possible. The number of columns in the first matrix must be equal to the number of rows in the second matrix.")
else:
    matrix2 = [[0 for _ in range(cols2)] for _ in range(rows2)]

    print("\n Enter the elements of matrix2")
    for i in range (rows2):
        for j in range (cols2):
            matrix2[i][j]= int((input(f"Enter element [{i}][{j}] of matrix2: ")))

    for r in matrix2:
        print (r)   
        
    matrix_multiplication = [[0 for _ in range(cols2)] for _ in range(rows1)]
    for i in range (rows1):
        for j in range (cols2):
            for k in range (cols1):
                matrix_multiplication[i][j] += matrix1[i][k] * matrix2[k][j]
                
    print("\n The resulting matrix is: ")
    for r in matrix_multiplication:
        print(r)