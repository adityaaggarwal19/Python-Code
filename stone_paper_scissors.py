import random
print("Welcome to stone paper and scissors game")
score_a=0
score_b=0
while(1):
        x=input("Stone Paper or Scissors? ")
        y=random.choice(["stone","paper","scissors"])
        if x==y:
            print("You both have", x)
        elif x=="paper" and y =="stone":
            print("Your paper stops the stone of computer")
            score_a=score_a+1
        elif x=="paper" and y =="scissors":
            print("Your paper is cutted by computer's scissors")
            score_b=score_b+1
        elif x=="stone" and y =="paper":
            print("Your stone is stopped by computer's paper")
            score_b=score_b+1
        elif x=="scissors" and y =="paper":
            print("Your scissors cut the computer's paper")
            score_a=score_a+1
        elif x=="stone" and y=="scissors":
            print("Your stone crashed the computer's scissors")
            score_a=score_a+1
        elif x=="scissors" and y =="stone":
            print("Your scissors are crashed by the computer's stone")
            score_b=score_b+1
        if score_a==10 or score_b==10:
            if score_a==10:
                print("You won the game :)")
                break
            else:
                print("You lost the game :(")
                break
        else:
            print("Next turn")