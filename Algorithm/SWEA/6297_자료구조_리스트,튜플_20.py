# 콤마 (,)로 구분해 숫자를 입력하고, 입력된 숫자 중 홀수를 콤마(,)로 구분해 출력하는
# 리스트 내포 기능을 이용한 프로그램을 작성하십시오.

lis = input('').split(', ')
lis = list(map(int, lis))
lis = [a for a in lis if a % 2 != 0]
for i in lis:
    if i != lis[-1]:
        print(i, end=', ')
    else:
        print(i)
