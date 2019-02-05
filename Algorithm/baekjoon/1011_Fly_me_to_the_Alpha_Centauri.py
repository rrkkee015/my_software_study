testcases=int(input())
for tc in range(testcases):
    x,y=tuple(map(int,input().split()))
    for i in range(0,2**31):
        if (i-1)**2<y-x<=i**2:
            num=i
            break
    upcnt=0
    dncnt=num
    while dncnt != 0:
        if y-x==num**2-upcnt:
            result=num*2-1
            print(result)
            break
        upcnt+=1
        dncnt-=1
    if dncnt==0:
        result=num*2-2
        print(result)