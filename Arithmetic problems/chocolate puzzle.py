N = 5
a = 2
r = 2
t = 0

# for i in range(1, N+1):
#     t = t+a
#     a = a * 2
# print(t)

t = a*(r**N-1)//(r-1)
print(t)