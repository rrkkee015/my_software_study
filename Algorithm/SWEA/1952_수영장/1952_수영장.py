import sys
sys.stdin = open('sample_input.txt','r')

def swim(month, cost):
    global min_
    if month >= 12:
        if min_ > cost:
            min_ = cost
        return
    elif cost > min_:
        return
    else:
        if plan[month] == 0:
            swim(month + 1, cost)
        else:
            swim(month + 1, cost + prices[0]*plan[month])
            swim(month + 1, cost + prices[1])
            swim(month + 3, cost + prices[2])

testcases = int(input())
for tc in range(testcases):
    prices = list(map(int,input().split()))
    plan = list(map(int,input().split()))
    min_ = prices[-1]
    swim(0, 0)
    print(f'#{tc+1} {min_}')


# 선생님 코드
# T = int(input())
# for tc in range(1, T+1):
#     day, month ,quarter, year = map(int, input().split())
#     arr = list(map(int,input().split()))
#     MIN = year
#
#     def calc(n, cost): # 고려해야하는 달, 비용
#         global MIN
#         if n >= 12:
#             MIN = min(MIN, cost)
#             return
#         if arr[n] == 0:
#             calc(n + 1, cost)
#         else:
#             calc(n + 1, cost + day * arr[n])
#             calc(n + 1, cost + month)
#             calc(n + 1, cost + quarter)

#
