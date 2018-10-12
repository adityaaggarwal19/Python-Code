from random import randint
def comp_call(a,b):
    return randint(a,b)
turn=0
x=0
while(1):
    if turn==0:
        x=int(input("Enter a Number"))
        if x==20:
            break
        else:
            turn=1
    if turn==1:
        y=comp_call(x+1,x+2)
        print(y)
        if y==20:
            break
        else:
            turn=0
        
        
