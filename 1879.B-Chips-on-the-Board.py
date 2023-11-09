for i in range(int(input())):
    z=int(input())
    l1=sorted(list(map(int,input().split())))
    l2=sorted(list(map(int,input().split())))
    s1=s2=0
    for j in range(z):
        s1+=l1[j]+l2[0]
        s2+=l2[j]+l1[0]
    print(min(s1,s2))
    
    
    
