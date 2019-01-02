# 1. 5명의 시험점수 값을 넣은 리스트를 만든다.
# 2. for문으로 각 점수가 60점이 넘나 안 넘나 확인한다
# 2-1. 넘으면 합격
# 2-2. 못 넘으면 불합격


# 1. 5명의 시험점수 값을 넣은 리스트를 만든다.
scores=[88,30,61,55,95]
#score=0
num =0
#for i in range(1,6):
#   score=int(input("점수를 입력하세요 :"))
#   scores.append(score)
for j in scores:
    num += 1
    if j < 60:
        print("{}번 학생은 {}점으로 불합격입니다.".format(num,j))
    else:
        print("{}번 학생은 {}점으로 합격입니다.".format(num,j))
