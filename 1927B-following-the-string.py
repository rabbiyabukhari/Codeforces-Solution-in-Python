#https://codeforces.com/problemset/problem/1927/B
def convertor(string,n):
    j=0
    while n!=0:
        x='0'
        for i in range(len(string)):
            if str.isnumeric(string[i]):
                if int(string[i])==int(x):
                    string[i]=chr(97+j)
                    x=str(int(x)+1)
                    n-=1
        j+=1
    print( "".join(string))
for _ in range(int(input())):
    n=int(input())
    string=list(map(str,input().split()))
    convertor(string,n)