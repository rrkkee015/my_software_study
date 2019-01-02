# 1. 100~300 숫자를 가진 numbers 리스트를 가진다.
# 2. 100의 자리를 2로 나눠서 0이 되는지 확인한다.
# 3. 10을 나눈 몫이 2로 나눠서 0이 되는지 확인한다.
# 4. 전체를 2로 나눠서 0이 되는지 확인한다.
# 5. 출력한 애들을 리스트에 담고 (,)를 소유시키고 출력한다.
numbers=[]
numbers_100=[]
numbers_10=[]
results=[]
for i in range(100,301):
    numbers.append(i)
for j in numbers:
    if (j//100)%2==0:
        numbers_100.append(j)
for k in numbers_100:
    if (k//10)%2==0:
        numbers_10.append(k)
for h in numbers_10:
    if h%2 ==0:
        results.append(h)
for y in results:
        if y !=results[-1]: # list[-1]이 list의 마지막 인덱스이다.
            print("%d,"%y, end='') # end에 빈 문자열을 지정하면 다음 번 출력이 바로 뒤에 오게 됨
        else:
            print(y)
