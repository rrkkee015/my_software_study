def dfs(x,y):
    if x == 0:
        ans = y
        return
    visited[x][y] = True
    if y - 1 >= 0 and arr[x][y-1] and not visited[x][y-1]:
        dfs(x, y-1)
    elif y + 1 < 100 and arr[x][y+1] and not visited[x][y+1]:
        dfs(x, y+1)
    else:
        dfs(x-1, y)

for tc in range(1, 11):
    case = int(input())

    arr = [list(map(int,input().split())) for _ in range(100)]
    sx = sy =0 # 시작점
    for _ in range(100):
        if arr[99][_] == 2:
            sx, sy = 99, _
            break
    visited = [[False] * 100 for _ in range(100)]
