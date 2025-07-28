print("The tunnel splits here.  Do you want to go left (1), or right (2)?")
k=input("choice:")
if k==("1"):
    print("you turn left into a pit of lava. GAME OVER")
if k==("2"):
    print("Being bold, you head right.  There's a bowl of candy!")
    a=input("do you want to eat any? yes 1 no 2")
if a==("1"):
    print("oh no! the candy is poisoned! you die! GAME OVER.")
if a==("2"):
    print("not touching the bowl, you move on.")
    b=input(" you come across another fork. do you go left 1 or right 2  ")
    if b==("1"):
        print("you head left and find a blue mushroom")
        c=input("you come closer to the mushroom and see that it is glowing. do you 1: leave it there or 2: pick it and use it for light?")
        if c==("1"):
            print("you decide to leave the mushroom. suddenly your flashlight stops working. since you cant see, you accidentally walk into a landmine. you die. GAME OVER")
        if c==("2"):
            print("you pick the mushroom and and it plays the sound of pennywise screaming... 'i will get you' you move on anyways")
            d=input("You find a ROBLOX gift card lying on a table. will you 1: take it or 2: leave it?")
            if d==("1"):
                print("you take the card and leave the room. right outside the room is the exit! you have made it to the end... even with a ROBLOX gift card!!! you go home to use it. CONGRADULATIONS! YOU WIN! TOTAL POINTS: 2358")
            if d==("2"):
                print("you step around the table, trying to avoid a trap. instead the trap is on the side! the side you step on. suddenly, a large rock drops from the ceiling and lands hard, making the walls collapse. GAME OVER. ")
    if b==("2"):
        print("you head right and come to a large opening in the cave, letting sunlight in. but... you have unfortunitely forgot your spf30 at home. you burn to death. GAME OVER")








