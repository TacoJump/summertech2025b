# for i in range(1,7):
    # print("a",end=" ")
    # for f in range(0,i):
        # print("a",end=" ")
    # print("")

# for i in range(1,7):
#     # print("a",end=" ")
#     for f in range(0,7-i):
#         print("a",end=" ")
#     print("")
    
# for i in range(1,6):
#     # print("a",end=" ")
#     for f in range(0,7-i):
#         print(" ",end=" ")
#     for t in range(0,i):
#         print("a  ",end=" ")
#     print("")

# for l in range(1,7):
#     # print("a",end=" ")
#     for m in range(0,l):
#         print(" ",end=" ")
#     for o in range(0,7-l):
#         print("a  ",end=" ")
#     print("")

for i in range(1,6):
    # print("a",end=" ")
    for f in range(0,7-i):
        print(" ",end=" ")
    for t in range(0,i):
        if t==0 or t==i-1:
            print("a  ",end=" ")
        else:
            print("   ",end=" " )

    print("")

for l in range(1,7):
    # print("a",end=" ")
    for m in range(0,l):
        print(" ",end=" ")
    for o in range(0,7-l):
        if o==0 or o==7-l-1:
            print("a  ",end=" ")
        else:
            print("   ",end=" ")
    print("")

