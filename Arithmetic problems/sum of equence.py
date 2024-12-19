
# X = 8
# Y = 23

X, Y = map(int,input().split())
# X = int(input())
# Y = int(input())
mth = X
nth = Y
sum = 0
for i in range (mth, nth+1, 5):
    sum = sum + i
print(sum)