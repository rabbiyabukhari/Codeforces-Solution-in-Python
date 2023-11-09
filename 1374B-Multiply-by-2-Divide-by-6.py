B. Multiply by 2, divide by 6q=int(input())
for i         
1374B-Multiply-by-2,-divide-by-6in range(q):
    num=int(input())
    cnt2=cnt3=0
    while num %2 == 0:
        num //= 2
        cnt2+=1
    while num %3 == 0:
        num //= 3
        cnt3+=1
    if num==1 and cnt2<=cnt3:
        print(2*cnt3-cnt2)
    else:
        print(-1)


