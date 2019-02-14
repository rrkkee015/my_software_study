import sys
sys.stdin = open("sample_input.txt", "r")

def dfs(s):
    visited[s] = True
    for k in range(1, V + 1):
        if graph[s][k] and not visited[k]:
            dfs(k)

TC = int(input())

for i in range(1, TC + 1):
    V_E = list(map(int, input().split()))
    V, E = V_E[0], V_E[1]

    lines = ''
    line = [0] * (2*E)
    for _ in range(E):
        lines += input() + ' '
    lines='1 3 1 4'

    for j in range(len(lines)):
        if j % 2 == 0:
            line[j//2] = int(lines[j])

    S_G = list(map(int, input().split()))
    S, G = 1, 4

    visited = [0] * (V + 1)
    graph = [[0] * (V + 1) for _ in range(V + 1)]
    for j in range(0, len(line), 2):
        graph[line[j]][line[j + 1]] = 1

    dfs(S)

    if visited[G] == 1:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')