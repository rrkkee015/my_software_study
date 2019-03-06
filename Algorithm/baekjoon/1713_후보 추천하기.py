N=int(input())
pics=[0]*N
cnt=[0]*101
x=0
stus=int(input())
rec=list(map(int,input().split()))
for _ in range(len(rec)):
    print(cnt)
    if rec[_] in pics:
        cnt[rec[_]][0]+=1
    else:
        if 0 in pics:
            cnt[rec[_]]=[1,_]
            pics[x]=rec[_]
            x+=1
        else:
            if cnt.count(min(cnt)) >= 2:

            else:
                for k in range(len(cnt)):
                    if min(cnt)==cnt[k]:
                        cnt[k]=0
                        pics[k]=rec[_]