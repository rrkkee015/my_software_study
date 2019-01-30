import sys
sys.stdin=open('input.txt','r')
testcases=int(input())
for test in range(testcases):
    n=int(input())
    real_result=''
    li = list(map(int,input().split()))
    result=[0]*n
    i=0
    for k in range(len(result)):
        result[k] = [li[i],li[i+1]]
        i+=2
    ##################
    dic={}
    for idx,value in enumerate(result):
        dic[value[0]]=idx
    ########
    for i in result:
        x=0
        nasa = [0] * n
        nasa[x]=i
        cnt=1
        for k in result:
            if i == k:
                continue
            if nasa[x][1] in dic.keys():
                x += 1
                nasa[x]=result[dic[nasa[x-1][1]]]
                cnt+=1
        if cnt == len(result):
            break
    for k in range(len(nasa)):
        for i in range(len(nasa[k])):
            real_result += str(nasa[k][i])+ ' '
    print(f'#{test+1} {real_result}')

# 보라에몽 코드
testcase = int(input())
for tc in range(testcase):
    num = int(input())
    ary = list(map(int, input().split()))
    a, s = [], []

    # 암수 리스트 업데이트
    for i in range(0, len(ary), 2):
        a.append(ary[i])
        s.append(ary[i+1])

    # 진행 방향 1 앞으로 2 뒤로
    stat = 1
    cur = a[0]
    ans = []
    fcheck = 0
    while len(ans) != len(ary):
        for j in range(len(a)):
            if stat == 1:
                # 앞으로 갈 때는 암에서 찾아서 수에 있는 수를
                if cur == a[j]:
                    ans.extend([a[j], s[j]])
                    cur = s[j]
                # for문 다 돌았는데, 뒤에 수가 없으면 방향 전환
                if fcheck > len(a):
                    stat = 2
                    cur = ans[0]
            elif stat == 2 and cur == s[j]:
                # 뒤에서 갈 때는 수에서 찾아서 암에 있는 수를
                ans = [a[j], s[j]] + ans
                cur = a[j]
        fcheck += 1

    print("#%d" % (tc+1), ' '.join(map(str, ans)))
