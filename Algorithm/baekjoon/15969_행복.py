def my_max(lis):
    result=-1
    for i in lis:
        if result<i:
            result=i
    return result

def my_min(lis):
    result=10000
    for i in lis:
        if result>i:
            result=i
    return result

stu=int(input())
scores=list(map(int,input().split()))
print(my_max(scores)-my_min(scores))