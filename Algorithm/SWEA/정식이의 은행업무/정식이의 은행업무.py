import sys
sys.stdin=open('sample_input.txt','r')

def bi_cal(lis):
    num=0
    for _ in range(len(lis)):
        if lis[::-1][_]=='1':
            num+=2**(_)
    return num

def th_cal(lis):
    num=0
    for _ in range(len(lis)):
        if lis[::-1][_]!='0':
            num+=3**(_)*int(lis[::-1][_])
    return num

def check(a,b):
    if a==b:
        return True

testcases=int(input())

for tc in range(testcases):
    bi=[]
    th=[]
    for _ in range(2):
        temp=input()
        for __ in temp:
            if _==0:
                bi+=[__]
            else:
                th+=[__]

    gotit=False
    for _ in range(len(bi)):
        if gotit==True:
            break
        bi_temp=bi[:]
        if bi_temp[_]=='1':
            bi_temp[_]='0'
        else:
            bi_temp[_]='1'
        bi_num=bi_cal(bi_temp)

        for _ in range(len(th)):
            th_temp=th[:]
            if th_temp[_]=='0':
                th_temp[_]='1'
                th_num=th_cal(th_temp)
                if check(bi_num,th_num):
                    gotit=True
                    break
                th_temp[_]='2'
                th_num=th_cal(th_temp)
                if check(bi_num,th_num):
                    gotit=True
                    break
            elif th_temp[_]=='1':
                th_temp[_]='0'
                th_num=th_cal(th_temp)
                if check(bi_num,th_num):
                    gotit=True
                    break
                th_temp[_]='2'
                th_num=th_cal(th_temp)
                if check(bi_num,th_num):
                    gotit=True
                    break
            else:
                th_temp[_] = '1'
                th_num = th_cal(th_temp)
                if check(bi_num, th_num):
                    gotit = True
                    break
                th_temp[_] = '0'
                th_num = th_cal(th_temp)
                if check(bi_num, th_num):
                    gotit = True
                    break
    print(f'#{tc+1} {bi_num}')