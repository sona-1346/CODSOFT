a=int(input("Enter The First Number:"))
b=int(input("Enter The Second Number:"))
n=int(input("Enter The Range Number:"))
print("1.Addition\n","2.Subtraction\n","3.Multiplication\n","4.Division\n")
for choice in range(n):
    choice=int(input("Enter Your Choice"))
    if choice==1:
        print(a+b)
    elif choice==2:
        print(a-b)
    elif choice==3:
        print(a*b)
    elif choice==4:
        if b!=0:
            print(a/b)
        else:
            print("Denominator should not be zero")
    else:
        print("Your Choice Is Not Found")
