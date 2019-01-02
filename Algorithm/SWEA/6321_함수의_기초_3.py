# 1. 숫자를 입력할 수 있게 한다.
# 2. 입력받은 숫자를 a라고 한다면 a가 a-1까지 나누어지는 수가 1말고 없으면 소수이다.
# 3. 소수가 아닐 경우엔 소수가 아닙니다.를 출력한다.
# 4. 소수인 경우엔 소수입니다.를 출력한다.

def sosu():
    number = int(input(''))
    lis = []
    for num in range(1,number):
        if number % num == 0:
            lis.append(num)
    if len(lis) == 1:
        return '소수입니다.'
    else:
        return '소수가 아닙니다.'

sosu = sosu()
print(sosu)


