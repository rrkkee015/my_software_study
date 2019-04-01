# 유향 그래프
def DFS(x):
    for _ in range(1, len(go[x])):
        if visited[go[x][_]]:
            visited[go[x][_]] = False
            print(go[x][_])
            DFS(go[x][_])
R = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
go = [[_] for _ in range(8)]
visited = [True] * 8

visited[1] = False
print(1)

for _ in range(0, len(R), 2):
    go[R[_]].append(R[_ + 1])

DFS(1)

# 무향 그래프
def DFS(x):
    for _ in range(len(go[x])):
        if go[x][_] == 1 and visited[_]:
            visited[_] = False
            print(_)
            DFS(_)

go = [[0] * 8 for _ in range(8)]
visited = [True] * 8
visited[1] = False

for _ in range(0, len(R), 2):
    go[R[_]][R[_ + 1]] = 1
    go[R[_ + 1]][R[_]] = 1

print(1)
DFS(1)
