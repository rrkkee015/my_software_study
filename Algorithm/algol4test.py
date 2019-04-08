def power_set_i():
    bit = [0, 0, 0]
    for i in range(2):
        bit[0] = i
        for j in range(2):
            bit[1] = j
            for k in range(2):
                bit[2] = k
                print(bit)


def power_set_b():
    arr = [1, 2, 3]
    n = len(arr)
    for i in range(1 << n):
        print('{', end =' ')
        for j in range(n+1):
            if i & (1 << j):
                print(arr[j], end = ' ')
        print('}')


def power_set_r(k):
    if k == N: print(a)
    else:
        a[k] = 1; power_set_r(k + 1)
        a[k] = 0; power_set_r(k + 1)


print('부분집합 반복문')
power_set_i()

print('부분집합 바이너리 카운팅')
power_set_b()

N = 3
a = [0] * N
print('부분집합 재귀문')
power_set_r(0)


def perm_i():  # for statement
    for i1 in range(1, 4):
        for i2 in range(1, 4):
            if i2 != i1:
                for i3 in range(1, 4):
                    if i3 != i1 and i3 != i2:
                        print(i1, i2, i3)


def construct_candidates(a, k, input, c):
    in_perm = [False] * N

    for i in range(k):
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(input):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates


def perm_r_1(a, k, input): #backtracking
    c = [0] * N

    if k == N:
        print(a[0] + 1, a[1] + 1, a[2] + 1)
    else:
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            perm_r_1(a, k + 1, input)


def perm_r_2(n, r):  #recursion
    if r == 0:
        print(t[0], t[1], t[2])
    else:
        for i in range(n - 1, -1, -1):
            arr[i], arr[n - 1] = arr[n - 1], arr[i]
            t[r - 1] = arr[n - 1]
            perm_r_2(n - 1, r - 1)
            arr[i], arr[n - 1] = arr[n - 1], arr[i]


def perm_r_3(k):  #recursion
    if k == R:
        print(arr[0], arr[1], arr[2])
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm_r_3(k + 1)
            arr[k], arr[i] = arr[i], arr[k]



def perm_r_4(k): #recursion
    if k == N:
        print(t[0], t[1], t[2])
    else:
        for i in range(N):
            if visited[i]: continue
            t[k] = arr[i]
            visited[i] = 1
            perm_r_4(k + 1)
            visited[i] = 0


def perm_rep1(n, r):  #중복 순열
    if r == 0:
        print()
    else:
        for i in range(n - 1, -1, -1):
            arr[i], arr[n - 1] = arr[n - 1], arr[i]
            t[r - 1] = arr[n - 1]
            perm_rep1(n, r - 1)  # 중복 허용
            arr[i], arr[n - 1] = arr[n - 1], arr[i]


def perm_rep2(k):  #중복 순열
    if k == R:
        print()
    else:
        for i in range(0, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm_rep2(k + 1)


print('순열 반복문')
perm_i()

N = 3
R = 3

print('순열 재귀문1')
a = [0] * N
perm_r_1(a, 0, 3)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


t = [0] * N
print('순열 재귀문2')
perm_r_2(N, R)


print('순열 재귀문3')
perm_r_3(0)


visited = [0] * N
print('순열 재귀문4')
perm_r_4(0)




def comb1(n, r):  #조합
    if r == 0:
        print()
    elif n < r:
        return
    else:
        t[r-1] = arr[n-1]
        comb1(n-1, r-1)
        comb1(n-1, r)


def comb2(k, s): # 조합
    if k == R:
        print()
    else:
        for i in range(s, N-R+k):
            t[k] = a[i]
            comb2(k + 1, i + 1)

def comb_rep1(n, r):  #중복조합
    if r == 0:
        print()
    elif n == 0:
        return
    else:
        t[r-1] = arr[n-1]
        comb_rep1(n, r-1)
        comb_rep1(n-1, r)


def comb_rep2(k, s): # 중복조합
    if k == R:
        print()
    else:
        for i in range(s, N):
            t[k] = a[i]
            comb_rep2(k + 1, i)
