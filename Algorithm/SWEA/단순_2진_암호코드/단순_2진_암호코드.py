import sys
sys.stdin=open('input.txt','r')

def find(num,start):
    start+=1
    for _ in range(start,len(num)):
        temp=''
        for __ in range(7):
            temp+=num[_+__]
        if temp in password:
            start=_
            next_start=_
            break
    for _ in range(start,len(num),7):
        temp=num[_:_+7]
        for __ in range(len(password)):
            if temp==password[__]:
                pass_.append(__)
    if len(pass_) ==8:
        return
    else:
        while pass_:
            pass_.pop()
        find(num,next_start)

testcases=int(input())
for tc in range(testcases):
    N,M=list(map(int,input().split()))
    mat=[]
    pass_=[]
    for _ in range(N):
        mat.append(input())
    password=['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
    for _ in mat:
        if '0'*M != _:
            word=_
            break
    find(word,-1)
    holsu=0
    jjaksu=0
    gumjeong=0
    suming=0
    for _ in range(len(pass_)):
        if _ == len(pass_)-1:
            gumjeong=pass_[_]
        elif _%2:
            jjaksu+=pass_[_]
        else:
            holsu+=pass_[_]
        suming+=pass_[_]
    if (holsu*3+jjaksu+gumjeong)<10 or (holsu*3+jjaksu+gumjeong)%10 == 0:
        print(f'#{tc+1} {suming}')
    else:
        print(f'#{tc+1} 0')
