t=int(input())
while t>0:
    s=input()
    l=s.split(" ")
    a=int(l[0])
    b=int(l[1])
    n=int(l[2])
    for i in range(0,n):
        if i%2==0:
            a=a*2
        else:
            b=b*2
    res=max(a,b)//min(a,b)
    print(res)
    t=t-1
