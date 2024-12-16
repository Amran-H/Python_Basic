n = int(input("Please enter the n's value: "))
# N = 50
# s = 0

# for i in range (1, N):
#     if i%3 == 0 or i%5==0:
#         s = s+i
# print(s) 


n1= (n-1)//3
n2= (n-1)//5
n3= (n-1)//15

s1 = n1 * (2*3+(n1-1)*3)//2
s2 = n2 * (2*5+(n2-1)*5)//2
s3 = n3 * (2*15+(n3-1)*15)//2

print(s1+s2-s3)