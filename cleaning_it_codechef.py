t=int(input())
while t>0:
    l=[]
    n,m=map(int,input().split())
    for i in range(0,n):
        l.append(i+1)
    k=list(map(int,input().split()))
    for i in range(0,len(k)):
        l.remove(k[i])
    if len(l)==0:
        print()
        print()
    elif len(l)==1:
        print(l[0])
        print()
    else:
        
        i=0
        while i<len(l):
            print(l[i],end=" ")
            i=i+2
        print()
        i=1
        while i<len(l):
            print(l[i],end=" ")
            i=i+2
    t=t-1
