t=int(input())
while t>0:
    n=input()
    n1=0
    n0=0
    for i in range(0,len(n)):
        if n[i]=="1":
            n1=n1+1
        else:
            n0=n0+1
    if n1==1 or n0==1:
        print("Yes")
    else:
        print("No")
    t=t-1
