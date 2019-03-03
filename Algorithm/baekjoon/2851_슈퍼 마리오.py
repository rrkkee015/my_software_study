def my_abs(x):
    if x==0:
        return 0
    elif x>0:
        return x
    elif x<0:
        return -x

def my_min(x):
    result=999999
    for i in range(len(x)):
        if x[i]<result:
            result=x[i]
    return result

def my_max(x):
    result=-1
    for i in range(len(x)):
        if x[i]>result:
            result=x[i]
    return result

score=[]
temp=[]
result=[]
for i in range(10):
    mushroom=int(input())
    score+=[mushroom]

for _ in range(9):
    score[_+1]=score[_+1]+score[_]

for __ in range(10):
    temp+=[my_abs(score[__]-100)]

min_=my_min(temp)

for ___ in range(10):
    if temp[___]==min_:
        result+=[score[___]]
print(my_max(result))
