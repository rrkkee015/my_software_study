import sys, collections
sys.stdin = open('sample_input.txt','r')

testcases = int(input())

for tc in range(testcases):
    # N과 M을 받습니다.
    N, M = list(map(int,input().split()))
    # N에서 +1, -1, *2, -10 네 가지를 사용하여서 최소 몇 번의 연산으로 M을 갈 수 있을까요?
    # 저는 이걸 BFS로 풀어보겠습니다.
    dq = collections.deque()
    dq.append([M, 0])
    visited = [1] * 1000001
    visited[M] = 0
    while dq:
        temp, cnt = dq.popleft()
        if temp == N:
            print(f'#{tc + 1} {cnt}')
            break
        if temp < 0 and temp > 1000000:
            continue
        else:
            if temp % 2 == 0: # 짝수일 때
                if temp - 1 >= 1 and visited[temp - 1]:
                    visited[temp - 1] = 0
                    dq.append([temp - 1, cnt + 1])
                if 1000000 >= temp + 1 and visited[temp + 1]:
                    visited[temp + 1] = 0
                    dq.append([temp + 1, cnt + 1])
                if 1000000 >= temp + 10 >= 0 and visited[temp + 10]:
                    visited[temp + 10] = 0
                    dq.append([temp + 10, cnt + 1])
                if temp // 2 >= 1 and visited[temp//2]:
                    visited[temp // 2] = 0
                    dq.append([temp // 2, cnt + 1])
            else: #홀수일 때
                if temp - 1 >= 1 and visited[temp - 1]:
                    visited[temp - 1] = 0
                    dq.append([temp - 1, cnt + 1])
                if 1000000 >= temp + 1  >= 0 and visited[temp + 1]:
                    visited[temp + 1] = 0
                    dq.append([temp + 1, cnt + 1])
                if 1000000 >= temp + 10 and visited[temp + 10]:
                    visited[temp + 10] = 0
                    dq.append([temp + 10, cnt + 1])