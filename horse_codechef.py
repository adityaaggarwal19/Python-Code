t=int(input())
while t>0:
    n=input()
    mi=99999999999
    l=list(map(int,input().split()))
    for i in range(0,len(l)-1):
        for j in range(i+1,len(l)):
            if abs(l[i]-l[j])<mi:
                mi=abs(l[i]-l[j])
    print(mi)
