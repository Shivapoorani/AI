c="Yes"
while(c!="No"):
    
    a=int(input("Enter the Num1: "))
    b=int(input("Enter the Num2: "))
    print("1.Add\n 2.Sub\n 3.Mul\n 4.Div: ")
    Choice=int(input("Enter the Choice: "))
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    if(Choice==1):
        print("Addition: ",add)
    elif(Choice==2):
        print("Subraction: ",sub)
    elif(Choice==3):
        print("Multiplication: ",mul)
    elif(Choice==4):
        print("Division: ",div)
    else:
        print("Wrong Choice")
    c=input("Do you want to continue(Yes/No): ")
    
