print("Enter the No.Of. Rows and Columns: ",end=" ")
m,n=[int(i) for i in input().split()]
m1=[]
print("Enter the value of the Matrix: ")
print()
for i in range(m):
    l=[int(i) for i in input().split()]
    m1.append(l)
print()
print()
print("Matrix Transpose: ")
print()
for j in range(m):
    for i in range(n):
        print(m1[i][j],end=" ")
    print()
