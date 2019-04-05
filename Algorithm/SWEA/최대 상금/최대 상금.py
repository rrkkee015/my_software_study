import sys
sys.stdin = open('input.txt','r')
import collections

testcases = int(input())
for tc in range(testcases):
    temp, swi = list(map(str,input().split()))
    num = []
    visited = [[0] * (10**(len(temp))) for _ in range(int(swi) + 1)]
    for _ in temp:
        num.append(_)
    dq = collections.deque()
    dq.append([num,-1])
    temp_result = []
    while dq:
        temp_num, depth = dq.popleft()
        depth += 1
        if depth == int(swi):
            temp_result.append(int(''.join(temp_num)))
            continue
        for i in range(len(temp)-1):
            for j in range(i+1, len(temp)):
                temp_temp = temp_num[:]
                temp_temp[i],temp_temp[j] = temp_temp[j],temp_temp[i]
                if visited[depth][int(''.join(temp_temp))] == 0:
                    visited[depth][int(''.join(temp_temp))] = 1
                    dq.append([temp_temp[:],depth])
    print(f'#{tc+1} {max(temp_result)}')