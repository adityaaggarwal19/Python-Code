t=int(input())
while t>0:
    n=int(input())
    a=list(map(int,input().split()))
    k=int(input())
    john=a[k-1]
    a=sorted(a)
    for i in range(0,len(a)):
        if a[i]==john:
            print(i+1)
    t=t-1
