# def still_my_number_one(x, cnt):
#     global min_
#     if x == 1:
#         if min_ > cnt:
#             min_ = cnt
#         return
#     elif x < 1:
#         return
#     else:
#         still_my_number_one(x-1, cnt + 1)
#         if x % 2 == 0:
#             still_my_number_one(x//2, cnt + 1)
#         elif x % 3 == 0:
#             still_my_number_one(x//3, cnt + 1)
#
# N = int(input())
# dp = [0]*(N+1)
# min_ = 0xfffff
#
# still_my_number_one(N,0)
# print(min_)

# 여기까지가 일반적인 Brute Force로 짠 코드인데 여기서 우리가 원하는 건 DP화 시키는 것이다.
# 그래서 우리는 Memoization을 사용하도록 하겠다.
# 결과가 들어오면 걔를 입력받아서 저장하도록 하자

# 이거는 바텀업이다.

N = int(input())
dp = [0] * (N + 1)
if N == 1:
    print(0)
elif N == 2:
    print(1)
else:
    dp[2] = 1
    dp[3] = 1
    for _ in range(4,N+1):
        if _ % 2 == 0 and _ % 3 == 0:
            dp[_] = min(dp[_//2], dp[_//3], dp[_-1]) + 1
        elif _ % 2 == 0:
            dp[_] = min(dp[_//2], dp[_-1]) + 1
        elif _ % 3 == 0:
            dp[_] = min(dp[_//3], dp[_-1]) + 1
        else:
            dp[_] = dp[_-1] + 1
    print(dp)

# 다시 풀어보기 == > 바텀 업

N = int(input())
dp = [0] * (N + 1)
if N == 1:
    print(0)
elif N == 2:
    print(1)
else:
    dp[2] = 1
    dp[3] = 1
    for _ in range(4, N + 1):
        temp_list = []
        if _ % 2 == 0:
            temp_list.append(dp[_//2] + 1)
        if _ % 3 == 0:
            temp_list.append(dp[_//3] + 1)
        temp_list.append(dp[_-1] + 1)
        dp[_] = min(temp_list)
    print(dp[N])