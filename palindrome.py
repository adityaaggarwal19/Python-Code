def palindrome (n):
    temp=n
    rev=0
    while(n>0):
        n1=n%10
        rev=rev*10+n1
        n=n//10
    if(temp==rev):
        Return(True)
    else:
        return(False)

n=int(input('Enter a Number')
res=palindrome (n)
if res:
    print("The given number is a palindrome!")
else:
    print("The given number isn't a palindrome!")
