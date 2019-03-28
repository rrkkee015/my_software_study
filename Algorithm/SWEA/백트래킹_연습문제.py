import time
s = time.time()
def back(depth, lis):
    depth += 1
    if sum(lis) == 10:
        print(lis)
    elif sum(lis) > 10:
        return
    else:
        for _ in li:
            if _ not in lis:
                tem = lis[:]
                tem[depth] = _
                back(depth, tem)

li = [1,2,3,4,5,6,7,8,9,10]
back(-1, [0 for _ in range(len(li))])
g = time.time()
def back(lis, depth, su):
    if su == 10:
        for i, _ in enumerate(lis):
            if _:
                print(li[i], end=' ')
        print()
    elif su > 10:
        pass
    elif depth == 10:
        pass
    else:
        for _ in [True, False]:
            back(lis + [_], depth + 1, su + li[depth] if _ else su)

back([],0,0)
e = time.time()

print(g-s)
print(e-g)

# 선생님 꺼
def backtrack(arr, k, n, sum):
    if sum > 10:
        return
    if k == n:
        if sum == 10:
            for j in range(n):
                if chk[j]:
                    print(arr[j], end=" ")
            print()
        return

    k += 1

    chk[k - 1] = 1
    backtrack(arr, k, n, sum + arr[k - 1])
    chk[k - 1] = 0
    backtrack(arr, k, n, sum)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chk = [0] * 10
backtrack(arr, 0, 10, 0)