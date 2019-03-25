from itertools import permutations

# import sys
# sys.setrecursionlimit(10**9)

def baby_gin(n, k): # 배열의 길이, k = 0 부터 시작
    if k == n:
        # print(arr)
        f = arr[:3]
        s = arr[3:]

        if f[2] - f[1] == 1 and f[2] - f[0] == 2 and s[2] - s[1] == 1 and s[2] - s[0] == 2:
            print(arr)
        elif f[2] == f[1] and f[1] == f[0] and s[2]-s[1]==1 and s[2] - s[0] == 2:
            print(arr)
        elif f[2]-f[1] == 1 and f[2]-f[0] == 2 and s[2] == s[1] and s[1] == s[0]:
            print(arr)
        elif f[2] == f[1] and f[1] == f[0] and s[2] == s[1] and s[1] == s[0]:
            print(arr)

    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            baby_gin(n, k+1)
            arr[k], arr[i] = arr[i], arr[k]

# arr = [1,2,4,7,8,3]
arr = [6,6,7,7,6,7]
# arr = [0,5,4,0,6,0]
# arr = [1,0,1,1,2,3]
baby_gin(6, 0)