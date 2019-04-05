import sys
sys.stdin = open('sample_input.txt','r')

def pay(month, cost):
    global min_
    # month가 12 이상이 되면 min와 비교 후 함수를 종료합니다.
    if month >= 12:
        if min_ > cost:
            min_ = cost
            return
    # 이 달에 수영장 이용계획이 없으면 month + 1, cost는 그대로 함수에 넘깁니다.
    elif plan[month] == 0:
        pay(month + 1, cost)
    # 그게 아니면 비용 체크를 합니다.
    else:
        # 하루치 계산을 전부 다하고 다음 달로 갑니다.
        pay(month + 1, cost + plan[month] * costs[0])
        # 한달 계산을 하고 다음 달로 갑니다.
        pay(month + 1, cost + costs[1])
        # 세달 계산을 하고 세달 뒤로 갑니다.
        pay(month + 3, cost + costs[2])

testcases = int(input())
for tc in range(testcases):
    # 비용 배열을 만드는데, 일 / 월 / 3개월 / 1년 순이다.
    costs = list(map(int,input().split()))
    # min 값을 미리 잡아주는데 min 값은 1년 결제권으로 잡아놓는다.
    min_ = costs[-1]
    # 12 개월 이용 계획을 받자, 인덱스는 0부터 11까지이다.
    plan = list(map(int,input().split()))
    # 1월부터 cost를 계산하는 함수를 적용합시다.
    # 인자로는 처음 개월, 비용을 넣습니다.
    pay(0, 0)
    # 결과를 출력합니다.
    print('#{} {}'.format(tc+1, min_))