def sec_lar(a,b,c):
    if a>b:
        if a>c:
            if c>b:
                print(c)
            else:
                print(b)
        else:
            print(a)
    else:
        if b>c:
            if c>a:
                print(c)
            else:
                print(a)
        else:
            print(b)
    return
t=int(input())
while t>0:
    n=input()
    l=list(n.split(" "))
    a=int(l[0])
    b=int(l[1])
    c=int(l[2])
    sec_lar(a,b,c)
    t-=1
