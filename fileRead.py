# python file operation using open, read, write, close

file2 = open("textFile2.txt", "w")
file2.write("Hi this a automated file.\nI generated this file using the write function.\nIt is the second day I am learning the file handling in Python.\nAnd it keeps on getting interesting!")


file2 = open("textFile2.txt", "a")
file2.write("\nHi, this is a new line")
file2.close

file2 = open("textFile2.txt", "r")
for i in file2:
    print(i)