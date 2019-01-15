t=int(input())
while t>0:
    n=int(input())
    a=n%10
    while n>0:
        b=n%10
        n=n//10
    print(a+b)
    t=t-1
