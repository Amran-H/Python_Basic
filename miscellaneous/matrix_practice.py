rows1 = int(input("Enter the number of rows of first matrix: "))
cols1 = int(input("Enter the number of columns of first matrix: "))

matrix1 = [[0 for _ in range(cols1)] for _ in range(rows1)]

for i in range(rows1):
    for j in range(cols1):
        matrix1[i][j]=int(input(f"Enter the {i}{j} elements of matrix1: "))
        
for r in matrix1:
    print(r)
        
rows2 = int(input("Enter the number of rows of second matrix: "))
cols2 = int(input("Enter the number of cols of second matrix: "))

matrix2 = [[0 for _ in range(cols2)]for _ in range(rows2)]

for i in range(rows2):
    for j in range(cols2):
        matrix2[i][j]=int(input(f"Enter the {i}{j} element of matrix2: "))
        
for r in matrix2:
    print (r)
    

if rows1 == rows2 and cols1 == cols2:
    result = [[0 for _ in range(cols1)]for _ in range(rows1)]
    
    for i in range(rows1):
     for j in range (cols1):
      result[i][j] = matrix1[i][j] + matrix2[i][j]
    
    print("Result")
    for r in result:
        print(r)
    
else:
    print("Cannot do addition as the matrices have different dimensions")