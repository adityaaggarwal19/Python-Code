print("Basic Calculator")
while(1):
    print("Select the basic operation to be performed:- ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Divisiom")
    ch=int(input("Enter the choice (1-4)"))
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    if ch==1:
        print(num1," + ",num2," = ",num1+num2)
    elif ch==2:
        print(num1," - ",num2," = ",num1-num2)
    elif ch==3:
        print(num1," * ",num2," = ",num1*num2)
    elif ch==4:
        print(num1," / ",num2," = ",num1/num2)
    else:
        print("You have entered a wrong choice!!!")
    l=input("Do you want to perform another operation (y/n)?")
    if l=='n':
        print("Thank for using the basic calculator :)")
        break