import sys
sys.stdin=open('sample_input.txt','r')

testcases = int(input())

def check(lis):
    global suming
    num=0
    lis=lis[::-1]
    for _ in range(len(lis)):
        if _ % 2 == 0:
            num+=lis[_]*3
        else:
            num+=lis[_]
    if num % 10 == 0:
        return True
    else:
        return False

for tc in range(testcases):
    # input 받기
    N,M = list(map(int,input().split()))
    mat=[]
    for _ in range(N):
        mat.append(input())

    password = ['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']

    # 16진수인 수를 2진수로 다 바꾸기
    for _ in range(len(mat)):
        mat[_] = mat[_].replace('0', '0000')
        mat[_] = mat[_].replace('1', '0001')
        mat[_] = mat[_].replace('2', '0010')
        mat[_] = mat[_].replace('3', '0011')
        mat[_] = mat[_].replace('4', '0100')
        mat[_] = mat[_].replace('5', '0101')
        mat[_] = mat[_].replace('6', '0110')
        mat[_] = mat[_].replace('7', '0111')
        mat[_] = mat[_].replace('8', '1000')
        mat[_] = mat[_].replace('9', '1001')
        mat[_] = mat[_].replace('A', '1010')
        mat[_] = mat[_].replace('B', '1011')
        mat[_] = mat[_].replace('C', '1100')
        mat[_] = mat[_].replace('D', '1101')
        mat[_] = mat[_].replace('E', '1110')
        mat[_] = mat[_].replace('F', '1111')

    # 암호를 추출한다.
    # 행을 뒤에서부터 찾으면서, 1을 만나면 암호의 시작이니까 체크를 해준다.
    # 암호는 1234 패턴을 지킨다. 1이 나오고 0이 나오고 1이 나오고 0이 나오는 순이다.
    # 단, 암호의 길이가 7개인지 14개인지 모르니 확인을 해야한다.

    result=[]
    for i in range(len(mat)):
        temp_num = 1 # 배수에 따른 숫자 정하기
        temp='' # 하나의 암호를 2 담을 변수
        cnt=0 # TFTF 패턴을 찾을 애 4321 순으로 진행하겠다.
        for j in range(len(mat[i])-1,-1,-1):
            if cnt == 0 and mat[i][j] == '1':
                cnt+=1
                temp = mat[i][j] + temp
            elif cnt == 1 and mat[i][j] == '1':
                temp = mat[i][j] + temp
            elif cnt == 1 and mat[i][j] == '0':
                temp = mat[i][j] + temp
                cnt+=1
            elif cnt == 2 and mat[i][j] == '0':
                temp = mat[i][j] + temp
            elif cnt == 2 and mat[i][j] == '1':
                temp = mat[i][j] + temp
                cnt+=1
            elif cnt == 3 and mat[i][j] == '1':
                temp = mat[i][j] + temp
            elif cnt == 3 and mat[i][j] == '0':
                temp = mat[i][j] + temp
                cnt+=1
            elif cnt == 4 and mat[i][j] == '0':
                temp = mat[i][j] + temp
            elif cnt == 4 and mat[i][j] == '1' and temp != '':
                result.append(temp)
                temp='1'
                cnt=1
        else:
            if temp != '':
                result.append(temp)

    for _ in range(len(result)):
        temp_num=''
        if _ % 8 == 0:
            temp = len(result[_]) // 7
        for __ in range(len(result[_])-1, -1 , -temp):
            temp_num = result[_][__] + temp_num
            if len(temp_num) == 7:
                break
        result[_]=temp_num

    for _ in range(len(result)):
        for __ in range(len(password)):
            if result[_]==password[__]:
                result[_]=__

    real_result=[]
    for _ in range(0, len(result), 8):
        if result[_:_+8] not in real_result:
            real_result.append(result[_:_+8])

    suming=0
    for _ in range(len(real_result)):
        checking = check(real_result[_])
        if checking == True:
            suming += sum(real_result[_])
    if suming == 0:
        print(f'#{tc+1} 0')
    else:
        print(f'#{tc+1} {suming}')

