import random
op=("rock","paper","scissor")
countuser=0
countcomputer=0
n=int(input("enter the range no:"))
for _ in range(n):
    user=input("enter ur choice:")
    computer=random.choice(op)
    print("ur choice:",user)
    print("com choice:",computer)
    if user=="rock" and computer=="scissor":
        print("user wins")
        countuser=countuser+1
    elif user=="scissor" and computer=="paper":
        print("user wins")
        countuser=countuser+1
    elif user=="paper" and computer=="rock":
        print("user wins")
        countuser=countuser+1
    elif user==computer:
        print("tie")
    else:
        print("com wins")
        countcomputer=countcomputer+1
        print("Final Score\nuser:",countuser,"\ncomputer",countcomputer)
        play=input("do u want to play again:")
        if play!="yes":
            break;
