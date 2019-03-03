N,M=tuple(map(int,input().split()))
cards=list(map(int,input().split()))
answer=0
cards_num=len(cards)
real_result=[]
answer=[0]

for i in range(1<<cards_num):
    result=[]
    for j in range(cards_num):
        if i & 1<<j:
            result+=[cards[j]]
            print(result)
    if len(result) == 3:
        if sum(answer)<sum(result)<=M:
            answer=result\
# for i in range(len(cards)-2):
#     for k in range(i+1,len(cards)-1):
#         for j in range(k+1,len(cards)):
#             if answer<cards[i]+cards[k]+cards[j]<=M:
#                 answer=cards[i]+cards[k]+cards[j]
# print(answer)