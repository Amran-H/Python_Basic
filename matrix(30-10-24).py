# # Function to take matrix input from the user
# def input_matrix(rows, cols):
#     matrix = []
#     print(f"Enter the elements of a {rows}x{cols} matrix:")
#     for i in range(rows):
#         row = []
#         for j in range(cols):
#             element = int(input(f"Enter element [{i}][{j}]: "))
#             row.append(element)
#         matrix.append(row)
#     return matrix

# # Take the dimensions of the matrices
# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of columns: "))

# # Input the matrices from the user
# print("Matrix 1:")
# matrix1 = input_matrix(rows, cols)
# for row in matrix1:
#     print(row)

# print("Matrix 2:")
# matrix2 = input_matrix(rows, cols)
# print(matrix2)

# # Initialize the result matrix with zeros
# result = [[0 for _ in range(cols)] for _ in range(rows)]

# # Perform matrix addition
# for i in range(rows):
#     for j in range(cols):
#         result[i][j] = matrix1[i][j] + matrix2[i][j]

# # Display the result
# print("Matrix Addition Result:")
# for row in result:
#     print(row)

a= [[5, 7, 10], 
    [4, 5, 2], 
    [1, 4, 1]]

b= [[10, 17, 9], 
    [8, 4, 7], 
    [3, 9, 11]]

c=[[0,0,0],[0,0,0],[0,0,0]]

print([a[0][0]*b[0][0], a[0][1]*b[1][0], a[0][2]*b[2][0]])
print([a[1][0]*b[0][1], a[1][1]*b[1][1], a[1][2]*b[2][1]])
print([a[2][0]*b[0][2], a[2][1]*b[1][2], a[2][2]*b[2][2]])


# for i in range(3):
#     for j in range(3):
#      c[i][j]=(a[i][j]+b[i][j])
# print(c)
