print("Welcome to 20 20")
turn=0
y=-1
while(1):
    if turn==0:
        x=int(input("Player A's turn"))
        if x==y+1 or x==y+2:
            if x==20:
                print("Player A won")
                break
            else:
                turn=1
        else:
            print("Please Enter the correct number")
    if turn==1:
        y=int(input("Player B's turn"))
        if y==x+1 or y==x+2:
            if y==20:
                print("Player B won")
                break
            else:
                turn=0
        else:
            print("Please Enter the correct number")
