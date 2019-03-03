def my_sum(x):
    result=0
    for __ in range(len(x)):
        result+=x[__]
    return result

def my_max(lis):
    result=-1
    for ___ in range(len(lis)):
        if result<lis[___]:
            result=lis[___]
    return result

scores=[]

for _ in range(5):
    cook=list(map(int,input().split()))
    scores+=[my_sum(cook)]

winner=my_max(scores)

for __ in range(5):
    if winner == scores[__]:
        print(__+1, end=' ')
        print(winner)