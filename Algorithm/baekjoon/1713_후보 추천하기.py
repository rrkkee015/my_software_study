N=int(input())
pics=[0]*N
cnt=[0]*101
order=[0]*101
x=0
stus=int(input())
rec=list(map(int,input().split()))
for _ in range(len(rec)):
    if rec[_] in pics: #사진틀에 사진 있는 경우
        cnt[rec[_]]+=1
    else:
        if 0 in pics: #사진틀에 빈 공간 있는 경우
            cnt[rec[_]]=1
            order[rec[_]]=_+1
            pics[x]=rec[_]
            x+=1
        else: #사진틀에 빈 공간 없는 경우
            min__=101
            for q in cnt:
                if q != 0 and min__> q:
                    min__=q
            if cnt.count(min__)>=2: #같은 점수가 2명 이상 있을 때
                min_=101
                for __ in range(1,len(cnt)):
                    if cnt[__]==min__:
                        if min_>order[__]:
                            min_=order[__]
                            min_index=__
                cnt[rec[_]]=1
                cnt[min_index]=0
                order[rec[_]]=_+1
                order[min_index]=0
                for ____ in range(len(pics)):
                    if pics[____]==min_index:
                        pics[____]=rec[_]
            else: #같은 점수가 없을 때
                for k in range(len(cnt)):
                    if min__==cnt[k]:
                        cnt[k]=0
                        cnt[rec[_]]=1
                        order[rec[_]]=_+1
                        for ___ in range(len(pics)):
                            if pics[___]==k:
                                pics[___]=rec[_]
for i in sorted(pics):
    if i==0:
        continue
    print(i, end=' ')