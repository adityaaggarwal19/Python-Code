a,b=map(int,input().split())
res=a-b
res=str(res)
l=""
n=0
for i in range(0,len(res)):
    if i==0:
        n=int(res[i])
        if n==1:
            n=n+1
        else:
            n=n-1
        l=l+str(n)
    else:
        l=l+res[i]
print(l)
