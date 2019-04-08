import sys
sys.stdin = open('input.txt','r')

testcases = int(input())
for tc in range(testcases):
    tc = int(input())
    cnt = [[_, 0] for _ in range(1001)]
    for _ in list(map(int,input().split())):
        cnt[_][1] += 1
    print('#{} {}'.format(tc, sorted(cnt, key = lambda x:(-x[1],-x[0]))[0][0]))