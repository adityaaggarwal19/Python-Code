a=[]
n= int(input("Enter the number of elements: "))
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ": "))
    a.append(element)
b=[sum(a[0:x+1]) for x in range(0,len(a))]
print("The Initial list is: ",a)
print("The final list is: ",b)n=int(input("Enter a number to be checked:- "))
temp=n
rev=0
while(n>0):
    n1=n%10
    rev=rev*10+n1
    n=n//10
if(temp==rev):
    print("The given number is a palindrome!")
else:
    print("The given number isn't a palindrome!")