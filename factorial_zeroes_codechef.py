t=int(input())
while t>0:
    count=0
    n=int(input())
    i=5
    while i<=n:
        a=n//i
        count=count+a
        i=i*5
    print(count)
    t=t-1

'''
import math
import re
t=int(input())
while t>0:
    count=0
    n=int(input())
    a=math.factorial(n)
    a=str(a)
    res=re.search('0*$',a)
    res=res.group()
    count=res.count("0")
    print(count)
    t=t-1

    i=5
    while i<=n:
        j=i
        while j>1:
            #count=count+1
            a=0
            a=a+1
            j=j/5
        if j==1:
            count=counta+
        else:
            count=count+1
        i=i+5
        
    a=fact(n)
    while a%10==0:
        count=count+1
        a=a//10
    print(count)
    t=t-1
'''
