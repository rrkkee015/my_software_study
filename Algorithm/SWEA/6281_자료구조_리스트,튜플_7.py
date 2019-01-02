# 다음의 결과와 같이 정수를 입력하면 리스트 내포를 이용해 약수 리스트를 출력하는 코드를 작성하십시오.

# 1. 입력을 받는다.
# 2. 리스트 내포를 이용하여 for문으로 순회시키고 0이되면 리스트에 넣는다.
# 3. 출력한다.

number = int(input(''))
numbers = [a for a in range(1, number+1) if number % a ==0]
print(numbers)
