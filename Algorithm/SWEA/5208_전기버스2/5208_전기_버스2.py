import sys
sys.stdin = open('sample_input.txt','r')

def elec(x, cnt):
    global min_
    if cnt > min_:
        return
    for _ in range(N_list[x]):
        x+=1
        if x >= N:
            if min_ > cnt:
                min_ = cnt
            return
        elec(x, cnt + 1)

testcases = int(input())
for tc in range(testcases):
    temp_lis = list(map(int,input().split()))
    N = temp_lis[0]
    N_list = [0] + temp_lis[1:]
    min_ = 0xffffff
    elec(1, 0)
    print(f'#{tc+1} {min_}')