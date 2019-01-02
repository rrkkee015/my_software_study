#사용자가 입력한 문장에서 공백을 이용해 단어들을 구분하고,
#중복된 단어 없이 단어를 콤마(,)로 구분해 사전순으로 출력하는 프로그램을 작성하십시오.

# 1. 일단 sorted를 사용해야하고, split(' ')을 사용해야함, 그리고 for문으로 돌려서 i가 lis에 있으면 출력이 안되도록 하자.
# 2. 인풋을 받을 리스트를 만들자.


lis = []
lis = input('').split(' ')
result = []
for i in lis:
    if i not in result:
        result.append(i)
result = sorted(result)
for j in result:
    if j == result[-1]:
        print(j)
    else:
        print(j,end=',')
