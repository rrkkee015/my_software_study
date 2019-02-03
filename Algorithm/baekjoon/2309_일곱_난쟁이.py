lis = [int(input()) for i in range(9)]
def my_sum(lis):
    result=0
    for i in lis:
        result+=i
    return result

def my_sorted(lis):
    for i in range(len(lis)-1,-1,-1):
        for j in range(0,i):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
    return lis

for i in range(1<<len(lis)):
    result = []
    for j in range(len(lis)):
        if i & 1<<j:
            result += [lis[j]]
    if my_sum(result) == 100 and len(result) == 7:
        result = my_sorted(result)
        for k in result:
            print(k)