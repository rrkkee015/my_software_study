# 동전 교환 문제
def coinChange(k, n):
    if n == 0:
        global Min
        Min = min(Min, k)
        print(sol[:k])
        return
    for val in coin:
        if val > n:
            continue
        sol[k] = val
        coinChange(k + 1, n - val)

coin = [6, 4, 1]
sol = [] * 100
Min = 0xfffff
coinChange(0, 8)