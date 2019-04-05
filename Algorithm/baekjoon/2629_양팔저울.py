chu = int(input())
chu_weight = list(map(int,input().split()))
goo = int(input())
goo_weight = list(map(int,input().split()))

check = [0 for _ in range(sum(chu_weight) + 1)]
check[0] = 1
temp = check[:]
for _ in chu_weight:
    for j in range(len(check)):
        if _ + j < len(check) and check[j] == 1:
            temp[_ + j] = 1
    check = temp[:]
for _ in chu_weight:
    for j in range(len(check)):
        if 0 <= j-_ and check[j] == 1:
            temp[j-_] = 1
    check = temp[:]
for _ in goo_weight:
    if _ > sum(chu_weight):
        print('N', end=' ')
        continue
    for __ in range(len(check)):
        if _ == __ and check[__] == 1:
            print('Y', end=' ')
            break
        elif _ == __ and check[__] == 0:
            print('N', end=' ')
            break
