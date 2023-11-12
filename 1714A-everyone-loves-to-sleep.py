for i in range(int(input())):
    n,h,m=map(int,input().split())
    acc=h*60+m
    w=24000
    for j in range(n):
        hr,mi=map(int,input().split())
        q=hr*60+mi
        if acc>q:
            s=23*60+60-acc+q
        else:
            s=q-acc
        if s<w:
            w=s
    print(w//60,w%60)
        
