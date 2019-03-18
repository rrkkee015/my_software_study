def counting(num):
    global n, cnt
    if num==n:
        cnt+=1
        return
    elif num>n:
        return
    else:
        for _ in lis:
            counting(num+_)

testcases=int(input())

for tc in range(testcases):
    n=int(input())
    cnt=0
    lis=[1,2,3]
    for i in lis:
        counting(i)
    print(cnt)