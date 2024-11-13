m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

matrix = [[0 for _ in range(n)]for _ in range(m)]

for i in range(m):
    for j in range(n):
        matrix[i][j]=int(input(f"enter the {i}{j} element of matrix: "))
       
for r in matrix:
    print(r)

def transpose(matrix):
    m, n = len(matrix), len(matrix[0])
    transposed_matrix = [[0]*m for _ in range(n)]
    
    for i in range (m):
        for j in range (n):
            transposed_matrix[j][i]=matrix[i][j]
            
    return transposed_matrix

print(transpose(matrix))