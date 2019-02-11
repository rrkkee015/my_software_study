N=input()
result=[int(i) for i in N]
cnt=[0 for i in range(9)]
for i in result:
    if i == 9:
        cnt[6]+=1
    else:
        cnt[i]+=1
cnt[6]=(cnt[6]+1)//2
max_=-1
for i in cnt:
    if max_<i:
        max_=i
print(max_)