print("Enter the No.Of. Rows and Columns: ",end=" ")
m,n=[int(i) for i in input().split()]
m1=[]
m2=[]
print("Enter the value of First Matrix: ")
print()
for i in range(m):
    l=[int(i) for i in input().split()]
    m1.append(l)
print()
print()
print("Enter the value of Second Matrix: ")
print()
for i in range(m):
    l=[int(i) for i in input().split()]
    m2.append(l)
print()
print()
print("Sum of the Matrices: ")
print()
for i in range(m):
    for j in range(n):
        print(m1[i][j]+m2[i][j],end=" ")
    print()
