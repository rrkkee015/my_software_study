# 1. 별 1개를 가진 애를 변수로 삼는다.
# 2. for 문을 돌려서 별이 하나씩 넣는다. 우측정렬 필수
# 3. 5개까지하고 출력한다.

result="*"
for i in range(1,6):
    if len(result) != 6:
        print("{:>5}".format(result))
        result = result + "*"
