#Write a recursive program to find out whether a number is odd or even
def oddeven(n):
    if n==0:
        return False
    elif n==1:
        return True
    else:
        return oddeven(n-2)
n=int(input("Enter a number: "))
if oddeven(n)==True:
    print("Number is Odd")
else:
    print("Number is Even")