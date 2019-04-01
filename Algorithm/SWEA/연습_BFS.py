import collections

R = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
visited = [True] * 8
route = [[0] * 8 for _ in range(8)]
dq = collections.deque()

for _ in range(0, len(R), 2):
    route[R[_]][R[_ + 1]] = 1
    route[R[_ + 1]][R[_]] = 1
visited[1] = False
dq.append(1)

while dq:
    v = dq.popleft()
    for _ in range(len(route[v])):
        if route[v][_] == 1 and visited[_]:
            print(_)
            visited[_] = False
            dq.append(_)