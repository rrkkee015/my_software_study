# 리스트 내포 기능을 이용해 [5, 6, 77, 45, 22, 12, 24]에서 짝수를 제거한 후 리스트를 출력하는 프로그램을 작성하십시오.

# 1. lis 라는 리스트를 만들고
# 2. lis를 %2 != 0으로 내포 함수로 거르고
# 3. 2를 출력한다.

lis = [5, 6, 77, 45, 22, 12, 24]
lis = [a for a in lis if a % 2 != 0]
print(lis)
