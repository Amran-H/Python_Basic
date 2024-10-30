# a = 4
# if a % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


#                                                                23/09/24

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))

# if  a+b == c+d:
#     print (" Two sides are equal")
# elif a+b > c+d:
#     print ("Left side is greater than the right one")
# else: 
#     print ("Left side is lesser than the right one")

# a = int(input("Enter a number: "))
# if  a > 0  :
#     print (" The number is positive")
# elif a < 0 :
#     print ("The number is negative")
# else :
#     print ("A is zero")


#                                                                25-09-24

# a = int(input("Enter a number: "))

# if a % 2 == 0:
#     print ("The number is even")
# else:
#     print("The number is Odd")

# a = str(input("Enter your command: "))

# if a == "on":
#     print("Light turn on")
# elif a == "off":
#     print("Light turn off")
# elif a == ("sleep"):
#         print("Light is not working")
# else :
#      print("Your command cannot be understood")

# /////LOOP
# sum = 0
# for i in range(3,11):
#     sum=sum+i
#     if i ==5:
#         break
# print(f"The total is: {sum}")

# for i in range(1,20):
#     if i%2==0:
#         print (f"{i} is Even")
#     else :
#         print(f"{i} is Odd")

# flag=0
# a = int(input("Enter a number: "))
# for i in range (2, a):
#     if a%i == 0:
#          flag=1
#          break   
# if flag==0:
#     print(f"{a} is prime number")
# else :
#     print(f"{a} is non prime")

# sum=0
# num = int(input("Enter number: "))
# for i in range (1, num+1):
#     a = int(input("Enter number: "))
#     sum+= a
# print(f"SUM: {sum}")
# avg=float(sum/num)
# print(f"avg = {avg}")

                                                    # 30-09-24

# for i in range(1,5):
#     for j in range(1,5):
#         print(j, end=" ")
#     print(" ")

# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print(" ")

# for i in range(5, 0, -1):
#     for j in range(1,i):
#         print("*", end=" ")
#     print(" ")

                                                    # 02-10-24

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print(" ")

# FUNCTION: A function is a block of statement that return the specific task.
# Two types of function: 1. Built in and 2. User defined
# Benefits of using functions: 1. Increase code reusability. 2. Increase code readability

# def printf():
#     print("Hello world")
# printf()

# def sum (a,b):
#     c=a+b
#     return c
# ans = sum(10, 20)
# print(f"the sum is {ans}")

# def evenOdd():
#     for num in range(1, 51):  
#         if num % 2 == 0:
#             print(f"Even numbers: {num}")
#         else:
#             print(f"Odd numbers: {num}" )
# evenOdd()

# def findEvenOdd(a):
#     if a%2==0:
#          print("Even number")
#     else:
#         print("Odd number" )
# findEvenOdd(9)

# def totalSum(num):
#     sum=0
#     for i in num:
#         sum+=i
#     print(sum)
    
# num=[2,4,5]
# totalSum(num)

# def printEven(num):
#     Even=[]
#     for i in num:
#         if i%2==0:
#             Even.append(i)
#     return Even
# num=[1,2,3,8,10,11,13,14,20]
# Even=printEven(num)
# print(Even)

# L=[1,2,"IIT", 5.5,1, True,]
# L.insert(0, 4)
# print(L)

# def evenOdd(num):
#     even=0
#     odd=0
#     for i in num:
#         if i%2==0:
#             even+=1
#         else:
#             odd+=1
#     print(f"Total even are: {even}")
#     print(f"Total odd are: {odd}")

# num=[10,20,30,40,9,3,8,5,2,1,17,78]
# evenOdd(num)



# ---------------------------------               05-10-24

# finding max value from a list

# def isMax(l):
#     Max=l[0]
#     for i in l:
#         if i>Max:
#             Max=i
#     print("The maximum number is:",Max)

# l=[5,10,100,25,50]
# isMax(l)

# def isLow(l):
#     min=l[0]
#     for i in l:
#         if i<min:
#             min=i
#     print("The minimum number is:",min)

# l=[1,5,10,25,50,0,-2, -1]
# isLow(l)

# def evenOddList(l):
#     even=[]
#     odd=[]
#     for i in l:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     print("Even numbers:",even)
#     print("Odd numbers:",odd)

# l=[1,2,3,4,5,6,7,8, 0,-1, -2,3]
# evenOddList(l)

# counting vowels in a word
# def countVowel(a):
#     count=0
#     vowels="a,e,i,o,u"
#     for i in a.lower():
#         if i in vowels:
#             count+=1
#     print(f"Number of vowels in {a} are:",count)

# a="Bangladesh"
# countVowel(a)

# A="Bangladesh"
# print(len(A))

# L=[5, 'THM', 6.5, True] 
# print(type(L[2]))


# ---------- MATH MODULE
# MM built in function  sqrt(x), pow(x,y), factorial(x), ceil(x), floor(x), fmod(x,y), fsum(x,y...), gcd(x,y), radians(), degrees(), prod()

# import math                     #Must import math module
# squareRoot=math.sqrt(64)
# print(squareRoot)

# s=math.pow(4, 3) #pow = power
# print("Power: ",s)

# fac = math.factorial(3)
# print("Factorial:",fac)

# print(math.ceil(4.76))
# print(math.floor(4.76))

# l=[1,2,3,4,5]
# print(math.fsum(l))
# print(math.prod(l))
# print(math.gcd(24,24))
# print(math.radians(57.29577951308232))
# print(math.degrees(0.017453292519943295))

# def squ(li):
#     s=[]
#     for i in li:
#         num=math.pow(i, 2)
#         s.append(math.ceil(num))
#     print(s)

# li=[1,2,3,4]
# squ(li)


#  ......................................................21-10-24

# numbers = []
# i=0
# print("How many numbers?")
# n=int(input())

# while i<n:
#     num=float(input(f"Enter number {i+1}:"))
#     numbers.append(num)
#     i=i+1

# max_value= max(numbers)
# min_value= min(numbers)

# print("Max number:",max_value)
# print("Min number: ",min_value)

# numbers = []
# greater_avg=[]
# i=0
# print("How many numbers?")
# n=int(input())
# sum=0

# while i<n:
#     num=float(input(f"Enter number {i+1}: "))
#     numbers.append(num)
#     i=i+1

# for i in numbers:
#     sum+=i
# average=sum/n

# for num in numbers:
#     if num > average:
#         greater_avg.append(num)

# print("Average is: ",average)
# print(greater_avg)

# .........................................................matrix

# rows=int(input("Enter the number of rows: "))
# cols=int(input("Enter the number of columns: "))

# matrix1=[[0 for _ in range (cols)] for _ in range(rows)]
# matrix2=[[0 for _ in range (cols)] for _ in range(rows)]

# print("\nEnter elements of first matrix:")
# for i in range (rows):
#     for j in range (cols):
#         matrix1[i][j] = int(input(f"Enter element [{i+1}][{j+1}] for matrix 1: "))

# print("\nEnter elements for the second matrix:")
# for i in range (rows):
#     for j in range (cols):
#         matrix2[i][j] = int(input(f"Enter element [{i+1}][{j+1}] for matrix 2: "))

# result_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

# for i in range(rows):
#     for j in range(cols):
#         result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

# print("\nTHe resulting matrix after summation is:")
# for row in result_matrix:
#     print(row)


# rows=int(input("Enter the number of rows: "))
# cols=int(input("Enter the number of columns: "))

# matrix=[[0 for _ in range (cols)] for _ in range(rows)]

# print("\nEnter elements of first matrix:")
# for i in range (rows):
#     for j in range (cols):
#         matrix[i][j] = int(input(f"Enter element [{i+1}][{j+1}] for matrix: "))

# sum = sum(sum(row)for row in matrix)
# elements = rows*cols
# avg = sum/elements
# for i in range (rows):
#     for j in range (cols):
#         if matrix[i][j]>avg:
#             print("elements greater than avg: ",matrix[i][j])
# print(sum, avg)

# Matrix multiflication, square


# .................................................23-10-24...............
# Recap for exam

# conditional statement
# a = input("Residency status: ")
# if a == "resident":
#     pay=500
# else:
#     pay=300
# print(pay)

# Loop
# for i in range(3):
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     c= a+b
#     print("The sum is ", c)

# for i in range (5, 11):
#     if i == 7:        #for skipping and to stop loop we use break
#         continue
#     for j in range (1, 11):
#      print(i, " x",j, "=", i*j)

#Function
# import math
# def sumSqrt (a,b):
#     c=a+b
#     return math.sqrt(c)
# print(sumSqrt(30,19))

# Lists
# an = ["orange", "Apple","Mango", "Banana"]
# print(an)


# ///////////////////////////////////////////  10-28-24 ///////////////////////////////////////////////

# my_list = [1,3, 4, 5, 2]
# even_sum = 0
# for i in my_list:
#     if i%2 == 0:
#      even_sum += i
# print(even_sum)

# my_list = [1,3, 4, 5, 2]
# for key, value in enumerate(my_list):
#    print(key, ":", value)

# my_list = [1,3, 4, 5, 2]
# for i in range(len(my_list)):
#    print(my_list[i])

# my_list = [1, 3, 4, 6, 1]
# index_sum=0
# for i in range(len(my_list)):
#     if i == 0:
#         continue
#     if i % 2==0:
#         index_sum+=my_list[i]
# print(index_sum)

# my_list=["apple", "mango", "banana", 'hi']

# my_list.clear()
# print(my_list)

# /////////////////////////         dictionary 
# student = {"name": "Akash", "age": 24}

# student["grade"] = "A+"
# print(student)


# -------------------------------------------------30-10-24 ---------------------------------
items_list = { 
               "Apple": 10,
               "Mango": 15,
               "Banana": 20,
               "Orange": 18
               }

# total_cost=0
# for item in items_list:
#     total_cost=sum(items_list.values())
# print(total_cost)

most_expensive_item = ""
most_expensive_price = 0
for item, price in items_list.items():
    if price > most_expensive_price:
        most_expensive_price =price
        most_expensive_item = item
print(items_list.items())

print(most_expensive_item, ":", most_expensive_price)

