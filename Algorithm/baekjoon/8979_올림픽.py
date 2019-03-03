N,K=list(map(int,input().split()))
scores=[]
for _ in range(N):
    scores+=[list(map(int,input().split()))]
# winner=sorted(scores, key=lambda score:(score[1],score[2],score[3]), reverse=True)
# temp=scores[0][1:4]
# present=1
# cnt=1
# scores[0]+=[present]
# for _ in scores[1:]:
#     if _[1:4]==temp:
#         _+=[present]
#         cnt+=1
#     else:
#         temp=_[1:4]
#         present+=cnt
#         _+=[present]
#         cnt=1
# for __ in scores:
#     if __[0]==K:
#         print(__[4])

for _ in scores:
    if _[0]==K:
        search=_

rank=1
for score in scores:
    if score != search:
        if score[1]>search[1]:
            rank+=1
        elif score[1]==search[1]:
            if score[2]>search[2]:
                rank+=1
            elif score[2]==search[2]:
                if score[3]>search[3]:
                    rank+=1
print(rank)