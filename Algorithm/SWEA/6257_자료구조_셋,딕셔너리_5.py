#리스트의 원소를 키로 하고, 그 원소의 length를 값으로 갖는 딕셔너리 객체를 생성하는 코드를 작성해봅시다.
#이 때 딕셔너리 내포 기능을 사용하며, 원소의 공백은 제거합니다.
#리스트 fruit는 다음과 같습니다. fruit = ['   apple    ','banana','  melon']

# 1.리스트 공백 없애는 방법 찾자 (string.replace(' ',''))
# 2.리스트를 만들자.
# 3.리스트 공백을 없앤 단어의 길이를 찾자
# 3.리스트 공백을 없앤 단어를 키로 삼고, 리스트 공백을 없앤 단어의 길이를 밸류로 삼는 딕셔너리를 만들자.

length=0
fruit = ['   apple    ','banana','  melon']
dic = {}
for i in fruit:
    length=len(i.replace(" ",""))
    dic.update({i.replace(" ",""):length})
print(dic)
