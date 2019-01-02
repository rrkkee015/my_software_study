#콤마(,)로 구분된 정수 값을 입력받아 리스트와 튜플 객체를 생성하는 코드를 작성하십시오.

# 1. 리스트 내포 함수로 input을 받을 수 있도록 split(', ')를 이용한다.
# 2. 그 입력받은 애를 튜플로 바꾼다.

lis = input('').split(', ')
lis = list(map(int, lis))
print(lis)
print(tuple(lis))
