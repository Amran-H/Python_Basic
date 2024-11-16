# Input dimensions of the first matrix
rows1 = int(input("Enter the number of rows of the first matrix: "))
cols1 = int(input("Enter the number of columns of the first matrix: "))

# Initialize the first matrix with zeros
matrix1 = [[0 for _ in range(cols1)] for _ in range(rows1)]

# Input elements for the first matrix
print("\nEnter elements of the first matrix:")
for i in range(rows1):
    for j in range(cols1):
        matrix1[i][j] = int(input(f"Enter element [{i+1}][{j+1}] for matrix 1: "))

# Input dimensions of the second matrix
rows2 = int(input("\nEnter the number of rows of the second matrix: "))
cols2 = int(input("Enter the number of columns of the second matrix: "))

# Check if matrix multiplication is possible
if cols1 != rows2:
    print("\nMatrix multiplication not possible. The number of columns in the first matrix must equal the number of rows in the second matrix.")
else:
    # Initialize the second matrix with zeros
    matrix2 = [[0 for _ in range(cols2)] for _ in range(rows2)]

    # Input elements for the second matrix
    print("\nEnter elements of the second matrix:")
    for i in range(rows2):
        for j in range(cols2):
            matrix2[i][j] = int(input(f"Enter element [{i+1}][{j+1}] for matrix 2: "))

    # Initialize the result matrix with zeros
    result_matrix = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    # Display the resulting matrix
    print("\nThe resulting matrix after multiplication is:")
    for row in result_matrix:
        print(row)
