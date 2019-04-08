def positioning(idx,s):
    if idx == 3:
        print(subset)
    for i in range(s+1, M):
        subset.append(i)
        positioning(idx+1, i)
        subset.pop()

subset = []
M = 6
positioning(0,-1)