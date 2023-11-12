for i in range(int(input())):
    x=int(input())
    z=bin(x)[2:]
    if z.count('1')>1:
        print("YES")
    else:
        print("NO")
