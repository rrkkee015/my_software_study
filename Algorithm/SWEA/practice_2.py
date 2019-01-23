import random
arr = [-3, 3, -9, 6, 7, -6, 1, 5, 4, -2]

n= len(arr)


result=[]
count=0
for i in range(1<<n): #공집합 빼려면 for i in range(1, 1<<n):
    for j in range(n):
        if i & (1<<j):
            result.append(arr[j])
    if sum(result)==0:
        count+=1
    result=[]
print(count-1)