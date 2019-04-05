import sys
sys.stdin = open('input.txt','r')

import collections

testcases = int(input())
for tc in range(testcases):
    # 숫자와 교환 횟수를 받습니다. 단 str로 받습니다.
    num, n = list(map(str,input().split()))
    # 사용하기 편하게 리스트로 변경합니다.
    num = list(num)
    # 결과값때 받을 result 배열을 만듭니다.
    result = []
    # bfs를 사용하기 위해서 deque을 만듭니다.
    dq = collections.deque()
    # 처음 수와 교환 횟수를 셀 cnt를 넣습니다.
    dq.append([num, 0])
    # 근데 만약 돌리기 전부터 그 수가 최대값이라면 굳이 bfs를 돌리지 않아도 됩니다.
    go = False # 검사할 숫자가 제일 큰 수인지 확인 하는 go
    go2 = False # 똑같은 숫자가 있는지 확인하는 go2
    for i in range(len(num) - 1):
        if num[i] == num[i + 1]: # 똑같은 숫자를 찾았다 !
            go2 = True
        if num[i] < num[i + 1]: # 만약 숫자가 점점 작아지는 수가 아니다
            break # 종료
    else: # 만약 숫자가 점점 작아지는 수이다.
        go = True
    # bfs를 돌립니다.
    if go == False:
        while dq:
            # 숫자와 교환 횟수를 받습니다.
            temp, cnt = dq.pop()
            # 만약 cnt가 바꿀 횟수만큼 돌았다면 result 배열에 추가합니다.
            if cnt == int(n):
                result.append(temp)
            # 만약 cnt가 자릿수 만큼 돌았다면은 그 수는 제일 큰 수가 될 것입니다. 걔를 넣고 while문을 종료합니다.
            if cnt == len(num):
                result.append(temp)
                continue
            else:
                # 순회를 위한 2중 포문을 만듭니다.
                for i in range(len(num) - 1):
                    for j in range(i + 1, len(num)):
                        # 잠시 걔를 다른 곳에 담고, 걔를 바꿔서 append를 합니다. 단 ! cnt 인덱스에 존재하는 값이 숫자 중에 제일 큰 값이어야 합니다.
                        temp_temp = temp[:]
                        temp_temp[i], temp_temp[j] = temp_temp[j], temp_temp[i]
                        if temp_temp[cnt] == max(temp_temp[cnt:]):
                            dq.append([temp_temp, cnt + 1])
        # 결과값에서 최대값을 구합니다.
        for _ in range(len(result)):
            result[_] = ''.join(result[_])
        print('#{} {}'.format(tc + 1, max(result)))
    # 만약 초장부터 제일 큰 수라면
    elif go == True:
        # 만약 바꾸는 횟수가 짝수면 그대로
        if go2:
            print('#{} {}'.format(tc + 1, ''.join(num)))
        # 홀수면 1의 자리와 10의 자리만 바꾸자
        elif int(n) % 2 != 0:
            num[-1], num[-2] = num[-2], num[-1]
            print('#{} {}'.format(tc + 1, ''.join(num)))