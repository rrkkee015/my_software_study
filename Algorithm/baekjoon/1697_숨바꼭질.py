from collections import deque

o, y = map(int,input().split())
if o > y:
    result = o - y
else:
    visited = [0] * 100001

    q = deque()
    visited[o] = 1
    q.append([o, 0])

    while q:
        po, t = q.popleft()
        if po == y:
            result = t
            break
        if po > y:
            if po - y != 1:
                continue
            else:
                visited[po - 1] == 1
                q.append([po - 1, t + 1])
                continue
        if po + 1 <= 100000 and visited[po + 1] == 0:
            visited[po + 1] = 1
            q.append([po + 1, t + 1])
        if 0 <= po - 1 and visited[po - 1] == 0:
            visited[po - 1] == 1
            q.append([po - 1, t + 1])
        if po * 2 <= 100000 and visited[po * 2] == 0:
            visited[po * 2] = 1
            q.append([po * 2, t + 1])
print(result)