a = [[1, 0, 2], 
     [2, 3, 5]]

b = [[2], 
     [4], 
     [5]]

c =[[0]*3, [0]*3, [0]*3]

for i in range(len(a)):
    for j in range(len(b[0])):
        c[i][j] = 0
        for k in range(len(b)):
            c[i][j] = c[i][j] + a[i][k] * b[k][j]
            
pr_str= ""            
for i in range (len(a)):
    for j in range (len(b[0])):
       pr_str = pr_str + str(c[i][j])
       
    pr_str = pr_str + "\n"
    print(pr_str)