import sys
sys.stdin = open('sample_input.txt','r')

# 연산자로 순열을 만들 함수를 만듭시다.
def dfs(ammo, temp_pm):
    # 만약 연산자 갯수를 모두 사용했으면 종료릅 합니다.
    if ammo == [0] * 4:
        # 그 값을 배열을 넣습니다.
        pm_order.append(temp_pm)
        return
    # 그게 아니라면 남은 연산자를 넣고 다시 재귀함수를 호출합시다.
    else:
        # ammo를 순회하면서 하나씩 차감하고 그 차감한 것을 인자로 넘깁시다.
        for _ in range(len(ammo)):
            # 만약 _가 0 이고 남은 연산자가 있으면 +를 넣고 넘깁시다, 0 위치의 갯수를 하나를 차감합시다.
            if _ == 0 and ammo[_] != 0:
                temp_ammo = ammo[:]
                temp_ammo[0] -= 1
                dfs(temp_ammo, temp_pm + '+')
            # 만약 _가 1 이고 남은 연산자가 있으면 -를 넣고 넘깁시다, 1 위치의 갯수를 하나를 차감합시다.
            if _ == 1 and ammo[_] != 0:
                temp_ammo = ammo[:]
                temp_ammo[1] -= 1
                dfs(temp_ammo, temp_pm + '-')
            # 만약 _가 2 이고 남은 연산자가 있으면 *를 넣고 넘깁시다, 2 위치의 갯수를 하나를 차감합시다.
            if _ == 2 and ammo[_] != 0:
                temp_ammo = ammo[:]
                temp_ammo[2] -= 1
                dfs(temp_ammo, temp_pm + '*')
            # 만약 _가 3 이고 남은 연산자가 있으면 /를 넣고 넘깁시다, 3 위치의 갯수를 하나를 차감합시다.
            if _ == 3 and ammo[_] != 0:
                temp_ammo = ammo[:]
                temp_ammo[3] -= 1
                dfs(temp_ammo, temp_pm + '/')

testcases = int(input())
for tc in range(testcases):
    N = int(input()) # 숫자 갯수
    pm = list(map(int,input().split())) # 연산자 갯수 '+' '-' '*' '/' 순으로 갯수다
    nums = list(map(int,input().split())) # 숫자카드
    pm_order = [] # 연산자 순열을 받을 배열
    # 연산자 갯수로 dfs를 돌립시다. 인자로는 연산자 갯수와 연산자를 받을 빈 문자열을 넘긴다.
    dfs(pm, '')
    # 연산자 순열을 다 만들었으니 이젠 계산을 해야합니다. max 값과 min 값을 만들고 비교를 합시다.
    max_ = -0xffffffffffff
    min_ = 0xfffffffffffff
    # 연산자를 순회하면서 연산자 기준 앞과 뒤의 숫자를 연산합시다.
    # 단 원본을 건들면 안되니 다른 숫자 배열을 만들어서 그 것을 사용하도록 합시다.
    for _ in pm_order:
        temp = nums[:]
        # 연산자의 위치가 중요하니 인덱스 기준으로 배열을 돕니다.
        for __ in range(len(_)):
            # 그 연산자가 더하기 일 때
            if _[__] == '+':
                temp[__ + 1] = temp[__] + temp[__ + 1]
            # 그 연산자가 빼기 일 때
            if _[__] == '-':
                temp[__ + 1] = temp[__] - temp[__ + 1]
            # 그 연산자가 곱하기 일 때
            if _[__] == '*':
                temp[__ + 1] = temp[__] * temp[__ + 1]
            # 그 연산자가 나누기 일 때
            # 문제가 이상한게 음수일 때 나누기가 답이 다르다. 이거를 처리해줍시다.
            if _[__] == '/':
                if temp[__] < 0:
                    temp[__ + 1] = -(- temp[__] //temp[__ + 1])
                else:
                    temp[__ + 1] = temp[__] // temp[__ + 1]
        # 연산을 마쳤으면 바로 min, max를 비교해줍니다.
        if min_ > temp[-1]:
            min_ = temp[-1]
        if max_ < temp[-1]:
            max_ = temp[-1]
    print('#{} {}'.format(tc + 1, max_ - min_))