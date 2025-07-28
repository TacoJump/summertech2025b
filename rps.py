from random import randint 
b=randint(1,3)
print("LET'S PLAY! JUST SO YOU KNOW, rock beats caterpillar, caterpillar beats leaf, and leaf beats rock. rock=1 leaf=2 caterpillar=3")
a=int(input("3...2...1...rock! leaf! caterpillar! says... SHOOT! (1,2,or 3?)"))
while a==(1,3):
    if a>3:
        print("ERROR! YOU CANNOT CHOOSE A NUMBER GREATER THAN 3! TRY AGAIN.")
        a=int(input("3...2...1...rock! leaf! caterpillar! says... SHOOT! (1,2,or 3?)"))
if a<1:
    print("ERROR! YOU CANNOT CHOOSE A NUMBER LESS THAN 1! TRY AGAIN.")
    a=int(input("3...2...1...rock! leaf! caterpillar! says... SHOOT! (1,2,or 3?)"))
if a==b:
    print("tie game!")
if a==1:
    print("your choice: rock")    
if a==2:
    print("your choice: leaf")
if a==3:
    print("your choice: caterpillar")
if a==1 and b==3:
    print("you won!they chose caterpillar")
if a==2 and b==1:
    print("you won! they chose rock")
if a==3 and b==2:
    print("you won! they chose leaf")
if a==3 and b==1:
    print("you lost! they chose rock")
if a==2 and b==3:
    print("you lost! they chose caterpillar")
if a==1 and b==2:
    print("you lost. they chose leaf")
