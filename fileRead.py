# python file operation using open, read, write, close

file = open("textFile2.txt", "r")
print(file.read())

file2 = open("textFile2.txt", "w")
file2.write("Hi this a automated file. I generated this file using the write function. It is the second day I am learning the file handling in Python. And it keeps on getting interesting!")

# file2 = open("textFile2.txt", "a")
# file2.write("Hi, this is a new line")