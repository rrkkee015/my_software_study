from sys import stdin

def algorithm(count):
    for x in range(N):
        if check[perm[x]]: continue
        temp = x
        while check[perm[temp]] != True:
            check[perm[temp]] = True
            temp = perm[temp] - 1
        count += 1
    return count

T = int(input())
result = list()

for x in range(T):
    N = int(stdin.readline())
    perm = [int(x) for x in stdin.readline().split()]
    check = [False]*(N+1)
    count = 0
    result.append(algorithm(count))

for x in result:
    print(x)