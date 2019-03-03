def my_max(lis):
    result=-1
    for _ in range(len(lis)):
        if result<lis[_]:
            result=lis[_]
    return result

N=int(input())
hills=list(map(int,input().split()))
s=hills[0]
g=hills[0]
result=[]
for _ in range(1,len(hills)):
    if g>=hills[_]:
        result+=[g-s]
        s=hills[_]
        g=hills[_]
    else:
        g=hills[_]
else:
    result+=[g-s]
print(my_max(result))