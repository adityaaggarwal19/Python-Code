t=int(input())
while t>0:
    res=0
    s=input()
    for i in range(0,len(s)):
        if s[i]=="4":
            res=res+1
    print(res)
    t=t-1
