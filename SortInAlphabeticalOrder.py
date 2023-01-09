a = input("Enter a Sentence: ")
l = a.split()  
for i in range(len(l)):
    for j in range(1,len(l)):
        if(l[j-1]>l[j]):
            s=l[j]
            l[j]=l[j-1]
            l[j-1]=s
for i in l:
    print(i,end=" ")
