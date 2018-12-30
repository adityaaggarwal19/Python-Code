t=int(input())
while t>0:
    n=input()
    l=list(n.split(" "))
    a=int(l[0])
    b=int(l[1])
    if a>b:
        print(">")
    elif a<b:
        print("<")
    else:
        print("=")
    t=t-1
