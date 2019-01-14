t=int(input())
while t>0:
    n=int(input())
    sum=0
    while n>0:
        sum=sum+(n%10)
        n=n//10
    print(sum)
    t=t-1
