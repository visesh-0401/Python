''' 
1 - snake
-1 - water 
0 - gun 
'''
import random

y=0
c=0

rounds = int(input("Enter the number of rounds you have to play: "))
while(rounds>0):
    computer = random.choice([1,-1,0])
    youstr = input("Enter your choice: ").lower()
    youDict = {"snake": 1, 
            "water": -1,
            "gun": 0}
    you = youDict[youstr]

    if(computer == -1 and you == 1):
        print("You WIN")
        y=y=1
    elif(computer == -1 and you == -1):
        print("TIE")
    elif(computer == -1 and you == 0):
        print("You LOSE")
        c=c+1

    elif(computer == 1 and you == 1):
        print("TIE")
    elif(computer == 1 and you == -1):
        print("You LOSE")
        c=c+1
    elif(computer == 1 and you == 0):
        print("You WIN")
        y=y+1

    elif(computer == 0 and you == 1):
        print("You LOSE")
        c=c+1
    elif(computer == 0 and you == -1):
        print("You WIN")
        y=y=1
    elif(computer == 0 and you == 0):
        print("TIE")

    rounds = rounds-1

print(f"Your points: {y}")
print(f"Computer points: {c}")

if(y>c):
    print("YOU WIN")
elif(c>y):
    print("YOU LOSE")
else:
    print("TIE")

