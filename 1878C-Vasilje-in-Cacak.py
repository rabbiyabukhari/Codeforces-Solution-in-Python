for i in range(int(input())):
    n,k,x=map(int,input().split())
    if (2*x>=k*(k+1)) and 2*x<=n*(n+1)-(n-k)*(n-k+1):
        print("YES")
    else:
        print("NO")
