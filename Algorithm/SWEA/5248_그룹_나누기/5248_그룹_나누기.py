def makeset(x):
    temp[x-1] = x

def findset(x):
    if x == temp[x-1]:
        return x
    else:
        return findset(temp[x-1])

def union(x,y):
    re = findset(y)
    for _ in range(len(temp)):
        if temp[_] == re:
            temp[_] = findset(x)

testcases = int(input())
for tc in range(testcases):
    N, M = list(map(int,input().split()))
    cls = list(map(int,input().split()))
    temp = [0] * N

    for _ in range(N):
        makeset(_+1)

    for _ in range(0, len(cls), 2):
        union(cls[_], cls[_ + 1])

    print(f'#{tc + 1} {len(set(temp))}')