def check_valid(a,i,p,l):
    if l>7:
        print("input too high! try again")
        return True
    if l==0:
        print("input invalid! try again")
        return True
    for k in range(5,-1,-1):
        if a[k][l-1]==0:
            if p==0:
                a[k][l-1]="O"
                break
            if p==1:
                a[k][l-1]="0"
                break
    if a[0][l-1]!=0:
        print("invalid. spot already taken.")
        return True
    return False
def update_board(a):
     for i in range(1,7):
        for f in range(1,8):
            if a[i-1][f-1]==0:
                print("|_|",end=" ")
            else:
                print("|"+a[i-1][f-1]+"|",end=" " )
        print("")
def win_check(a):
    for i in range(0,3):
        for j in range(0,7):
            if a[i][j]==a[i+1][j]==a[i+2][j]==a[i+3][j]:
                if a[i][j]=="O":
                    print("player 2 wins!!!")
                    return False
                if a[i][j]=="0":
                    print("player 1 wins!!! ")
                    return False   
    for i in range(0,6):
        for j in range(0,4):
            if a[i][j]==a[i][j+1]==a[i][j+2]==a[i][j+3]:
                if a[i][j]=="O":
                    print("player 2 wins!!!")
                    return False
                if a[i][j]=="0":
                    print("player 1 wins!!!")
                    return False    
    for i in range(0,3):
        for j in range(0,4):
            if a[i][j]==a[i+1][j+1]==a[i+2][j+2]==a[i+3][j+3]:
                if a[i][j]=="O":
                    print("player 2 wims!!!")
                    return False
                if a[i][j]=="0":
                    print("player 1 wins!!!")
                    return False
    for i in range(0,3):
        for j in range(3,7):
            if a[i][j]==a[i+1][j-1]==a[i+2][j-2]==a[i+3][j-3]:
                if a[i][j]=="O":
                    print("player 2 wins!!!")
                    return False
                if a[i][j]=="0":
                    print("player 1 wins!!!")
                    return False
    return True
                    
            
a=[]
score=0
for i in range(1,7):
    h=[]
    for f in range(1,8):
        h.append(0)
        print("|_|",end=" ")
    print("")
    a.append(h)
print(a)
r=True
while r==True:
    l=int(input("COLUMN:"))
    score+=1
    p=score%2
    if check_valid(a,i,p,l)==True:
        score-=1
        continue

    r=win_check(a)
    
    print(a)
    update_board(a)

    # if a[0][1]==a[1][1]==a[2][1]:
    #     if a[0][1]=="o":
    #         print("player 1 wins!!!")
    #         # l=9

    # score+=1
    # p=score%2
        