"""
파이썬 dictionary 활용 기초!
"""

# 1. 평균을 구하세요.
iu_score = {
    "수학": 80,
    "국어": 90,
    "음악": 100
}
# 1. dictionary에서 value값만 뽑자
# 2. 뽑아낸 값들의 합을 구한다
# 3. 총합을 갯수로 나눈다.

# 선생님 답변
# total_score = 0
# count = 0
# for score in iu_score:
#   total_score = total_score + iu_score[score]
#   count = count + 1
# print(total_score/count)

## 다른 답변
## 1. 검색하기 (python get(python 동사까진 고정) values in dict)
## 2. list(iu_score.values()) => dict에서 value값만 가져오는 법
## scores = iu_score.values() => dict_values([80, 90, 100])
## scores = list(iu_score.values()) =>[80, 90, 100]
## 3for num in scores: 해도 되지만 다른 방법을 찾아보자
## 4. 검색하기 (python get sum of list)
## print(sum(scores)) => 270 잘 나옴 => 이제 갯 수 구하는 법 찾아야함.
## 5. 검색하기 (python get length of list)
## length = len(scores)
## 결과 : print(sum(scores)/len(scores))

# 내 답변
result_1 = 0
for i in iu_score:
    result_1 += iu_score[i]
print(result_1/len(iu_score))

print("----------------------------------")


# 2. 반 평균을 구하세요.
score = {
    "iu": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "ui": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    }
}
# 1. 각 반을 순회하는 반복문을 작성한다.
# for cl in score:
# 2. 한 번 순회를 할 때 1번에서 작성한 코드를 활용한다.
# tmp = sum(list(score[cl].values()))
# lenght = len(list(score[cl].values()))
# 3. 출력한다.
# print("{}:{}".format(cl, tmp/lenght))

# 선생님 답변
#for cl in score:
#    tmp = sum(list(score[cl].values()))
#    lenght = len(list(score[cl].values()))
#    print("{}:{}".format(cl, tmp/lenght))


# 내 답변
result_2 = 0
result_2_1 = 0
result_2_2 = 0
for i in score['iu']:
    result_2_1 += score['iu'][i]
for j in score['ui']:
    result_2_2 += score['ui'][j]
print(result_2_1/len(score['iu']))
print(result_2_2/len(score['ui']))

print("-------------------------")

# 3. 도시별 최근 3일의 온도 평균은?
cities = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9],
}

"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""

# 1. 각 도시를 순회하는 반복문을 작성한다.
# for city in cities:
#   temp = cities[city] # 이 자체가 리스트라서 바로 사용하면 된다.
# 2. 1번의 코드를 활용하여 순회할 때마다 평균 값을 출력한다.
#   print("{}의 평균기온: {}".format(city, sum(temp)/len(temp)))
# 3. 답이 너무 더럽게 나와서 정리하는 방법을 검색해보자
# 4. python get round/ceil/floor value (round가 반올림)
# 5. round(변수, 1) 변수를 첫째자리가 나오도록 반올림해라
#   print("{}의 평균기온: {}".format(city, round(sum(temp)/len(temp),1)))
# 6. {:앞에 빈칸 갯수.몇 번째 자리 갯수f}를 해라
#   print("{}의 평균기온: {:.2f}".format(city, sum(temp)/len(temp)))


# 3-1. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
# 1. 최저기온, 최고기온을 저장할 수 있는 변수를 선언한다. (이거 서순 중요한 반복문 안에다가 하면 반복 할 때마다 선언을 해버림)
# 2. 각 도시를 순회하는 반복문을 만든다.
# 3. 각 도시의 기온 정보를 순회하는 반복문을 만든다.
# 4. 순회하다가 최저기온의 경우에는 현재 저장된 값보다 작은값이,
#    최고 기온의 경우에는 현재 저장된 값보다 큰 값이 있는 경우
#    현재 저장되어 있는 데이터를 교체한다.


# 선생님 답변
# 1. minimum = ["도시명", 1000], maximum =["도시명", -1000]
#   근데 키 값 원하는 value 값에 맞춰서 어케 바꿔 ?
# 2. for city in cities:
# 3.    for temp in cities[city]: #해당하는 value값을 뽑기 위해서, 이렇게 하면 기온은 구할 수 있지만 그 곳이 어딘지 모른다.
# 4. 최고기온에 해당하는 조건문
#    if(maximum[0] < temp):
#         maximum[0] = city
#         maximum[1] = temp
#    최저기온에 해당하는 조건문
#    if(minimum[1] > temp):
#         minimum[0] = city
#         minimum[1] = temp
# print("최고 기온은 {}의 {}도이며, 최저 기온은 {}의 {}도이다.".format(maximum[0],maximum[1],minimum[0],minimum[1]))
# 근데 최대값, 최소값 구하는건 없을까? 검색해보자 python get max value in list
# max(list), min(list)하면 된다. "서울"의 max, min / "대전"의 max, min / "광주"의 max, min / "부산"의 max, min을 순회하면 8번 밖에 안함


# 4. 위에서 서울은 영상 2도였던 적이 있나요?
# 1. cities 변수에서 서울의 리스트만 추출한다.
# 1-1. flag 라고 하는 변수에 false 저장한다.
# 2. 서울 리스트 내부를 순회하면서 if 문으로 2도가 있으면 True를 출력한다.
# 3. 2도 같았던 적이 있다면 flag 변수를 true로 바꿔준다.
# 4. flag 변수에 따라 출력물을 작성한다.

