import sys
sys.stdin=open('input.txt','r')

def find(num):
    for _ in range(len(num)):
        temp=''
        for __ in range(7):
            temp+=num[_+__]
        if temp in password:
            start=_
            break
    for _ in range(start,len(num),7):
        if len(num[_:])<7:
            return
        else:
            temp=num[_:_+7]
            for __ in range(len(password)):
                if temp==password[__]:
                    print(__,end=' ')

testcases=int(input())
for tc in range(testcases):
    N,M=list(map(int,input().split()))
    mat=[]
    for _ in range(N):
        mat.append(input())
    password=['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
    for _ in mat:
        if '0'*M != _:
            word=_
            break
    print(word)
    print(f'{tc}')