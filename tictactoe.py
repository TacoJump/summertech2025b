def check_valid(c,d,a,k):
    if c and d>3:
        print("input invalid. try again")
        return True
    a[c-1][d-1]
    if a[c-1][d-1]==0:
        if k==0:
            a[c-1][d-1]="x"
        if k==1:
            a[c-1][d-1]="o"
    else:
        print("spot is taken. try again.")
        return True
    return False 
def update_board(a):
     for i in range(1,4):
        for f in range(1,4):
            if a[i-1][f-1]==0:
                print("|_|",end=" ")
            else:
                print("|"+a[i-1][f-1]+"|",end=" " )
        print("")
def win_check(a,k):
    if a[0][1]==a[1][1]==a[2][1]:
        if a[0][1]=="o":
            print("player 1 wins!!!")
            return False
        if a[0][1]=="x":
            print("player 2 wins!!!")
            return False
    if a[0][0]==a[1][0]==a[2][0]:
        if a[0][0]=="o":
            print("player 1 wins!!!")
            return False
        if a[0][0]=="x":
            print("player 2 wins!!!")
            return False
    if a[0][2]==a[1][2]==a[2][2]:
        if a[0][2]=="o":
            print("player 1 wins!!!")
            return False
        if a[0][2]=="x":
            print("player 2 wins!!!")
            return False
    if a[0][0]==a[0][1]==a[0][2]:
        if a[0][0]=="o":
            print("player 1 wins!!!")
            return False
        if a[0][0]=="x":
            print("player 2 wins!!!")
            return False
    if a[1][0]==a[1][1]==a[1][2]:
        if a[1][0]=="o":
            print("player 1 wins!!!")
            return False
        if a[1][0]=="x":
            print("player 2 wins!!!")
            return False
    if a[2][0]==a[2][1]==a[2][2]:
        if a[2][0]=="o":
            print("player 1 wins!!!")
            return False
        if a[2][0]=="x":
            print("player 2 wins!!!")
            return False
    if a[0][0]==a[1][1]==a[2][2]:
        if a[0][0]=="o":
            print("player 1 wins!!!")
            return False
        if a[0][0]=="x":
            print("player 2 wins!!!")
            return False
    if a[0][2]==a[1][1]==a[2][0]:
        if a[0][2]=="o":
            print("player 1 wins!!!")
            return False
        if a[0][2]=="x":
            print("player 2 wins!!!")
            return False
    return True
a=[]
score=0
for i in range(1,4):
    h=[]
    for f in range(1,4):                                          
        h.append(0)
        print("|_|",end=" ")
    print("")
    a.append(h)
print(a)
l=True
while l==True:
    c=int(input("row:"))
    d=int(input("column:"))
    
    score+=1
    k=score%2
    if check_valid(c,d,a,k)==True:
        score-=1
        continue

    print(a)
    update_board(a)

    l=win_check(a,k)
    if score==9:
        l=False

