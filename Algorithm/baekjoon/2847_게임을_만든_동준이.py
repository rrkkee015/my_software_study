N=int(input())
scores=[int(input()) for _ in range(N)]
result=0
for _ in range(N-1,0,-1):
    if scores[_-1]>=scores[_]:
        temp=scores[_]-1
        result+=scores[_-1]-temp
        scores[_-1]=temp
print(result)