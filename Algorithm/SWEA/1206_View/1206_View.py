import sys
sys.stdin = open('input.txt','r')

for tc in range(10):
    N = int(input())
    buildings = list(map(int,input().split()))
    cnt = 0
    # for _ in range(2, N-2):
    #     bu_5 = buildings[_-2:_+3]
    #     if buildings[_] != max(bu_5):
    #         continue
    #     else:
    #         cnt += sorted(bu_5)[-1] - sorted(bu_5)[-2]
    # print('#{} {}'.format(tc + 1, cnt))
    index = 2
    while index < N - 2:
        bu_5 = buildings[index-2:index+3]
        if buildings[index] != max(bu_5):
            index += 1
            continue
        else:
            cnt += sorted(bu_5)[-1] - sorted(bu_5)[-2]
            index += 3
    print('#{} {}'.format(tc + 1, cnt))