import random
print("Welcome to 20 20")
score0=0
score1=0
while(1):
    print("Player A started the innings")
    x=random.choice([0,1,2,3,4,6])
    score0=score0+x
    if x==1 or x==2 or x==3:
        print("You have scored ",x," runs!")
    elif x==4:
        print("The ball ran towards the boundary for ",x," runs")
    elif x==0:
        print("Sorry you got out!")
        print("Your score is ",score0," runs")
        break    
    else:
        print("You have hit a six!")
    
while(1):
    print("Player B started the innings")
    x=random.choice([0,1,2,3,4,6])
    score1=score1+x
    if x==1 or x==2 or x==3:
        print("You have scored ",x," runs!")
    elif x==4:
        print("The ball ran towards the boundary for ",x," runs")
    elif x==0:
        print("Sorry you got out!")
        print("Your score is ",score1," runs")
        break    
    else:
        print("You have hit a six!")
if score0>score1:
    print("Player A won the match")
else:
    print("Player B won the match")
