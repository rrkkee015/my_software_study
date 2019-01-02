#다음의 결과와 같이 정수를 입력하면 약수를 리스트에 추가해 출력하는 코드를 작성하십시오.

# 1. 수를 입력받는다.
# 2. 입력 받은 수를 변수에 담아서 1부터 변수까지의 리스트를 만든다.
# 3. 리스트를 돌리면서 input 수를 나누고 % 0이되는 수를 만든다.

number = int(input(''))
lis=[]
for i in range(1,number + 1):
           if number%i ==0:
                      lis.append(i)
print(lis)
