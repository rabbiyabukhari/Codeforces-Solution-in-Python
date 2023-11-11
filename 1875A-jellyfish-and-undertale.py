for i in range(int(input())):
    a,b,n=map(int,input().split())
    lst=list(map(int,input().split()))
    z=b
    for num in lst:
        z+=min(num,a-1)
    print(z)
    
    
