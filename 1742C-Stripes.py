for i in range(int(input())):
    q=False
    lst=[]
    I=input()
    for w in range(8):
        x=input()
        lst.append([*x])
    for i in range(0,8):
        if ["R"]*8==lst[i]:
            print("R")
            q=True
            break
    if q==False:
        print("B")
