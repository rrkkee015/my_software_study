def stair(lis):
    global cnt
    for _ in range(1,4):
        o = lis[:] + [lis[-1] + _]
        if o[-1] == des:
            print(lis+[des])
            cnt+=1
        elif o[-1] > des:
            return
        else:
            stair(o)

lis = [0]
des = 4
cnt=0
stair(lis)
print(cnt)

def stair(n,li):
    if n == 0:
        print(li)
        return li
    elif n <0:
        pass
    else:
        for i in range(1,4):
            new_li = li +[n]
            stair(n-i,new_li)

stair(4,[])