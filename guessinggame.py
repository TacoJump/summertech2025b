from random import randint 
a=randint(1,100)
c=0
print("Guess a number between 1 and 100")
b=int(input("YOUR GUESS:"))
while b!=a:
    if b>100:
        print("not in range. try again")
        b=int(input("YOUR GUESS:"))
    if b<1:
        print("not in range. try again.")
    if b>100:
        print("not in range. try again")
        b=int(input("YOUR GUESS:"))
    if b==a:
        print("correct")
    if b>a:
        print("too high. guess again")
        b=int(input("YOUR GUESS:"))
        c+=1
    if b<a:    
        print("too low. guess again")
        b=int(input("YOUR GUESS:"))
        c+=1
    if b==a:
        print("you did it after all of your long and annoying guesses! count:"+str(c))
    