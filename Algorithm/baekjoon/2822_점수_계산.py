def my_sort(lis):
    for i in range(len(lis)-1,0,-1):
        for j in range(0,i):
            if lis[j][0]<lis[j+1][0]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
    return lis

def my_sort2(lis):
    for i in range(len(lis)-1,0,-1):
        for j in range(0,i):
            if lis[j][1]>lis[j+1][1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
    return lis

def my_sum(lis):
    result=0
    for i in lis:
        result+=i[0]
    return result

scores=[0]*8
for _ in range(8):
    scores[_]=[int(input()),_+1]
scores=my_sort(scores)
scores=scores[:5]
print(my_sum(scores))
scores=my_sort2(scores)
for _ in scores:
    print(_[1],end=' ')