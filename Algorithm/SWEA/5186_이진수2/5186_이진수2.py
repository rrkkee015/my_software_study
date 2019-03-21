import sys
sys.stdin=open('sample_input.txt','r')

testcases=int(input())

for tc in range(testcases):
    num=float(input())
    result=''
    while True:
        num*=2
        if num>=1:
            num-=1
            result+=str(1)
        else:
            result+=str(0)
        if num == 0 or len(result) >=13:
            break
    if len(result)>=13:
        print(f'#{tc+1} overflow')
    else:
        print(f'#{tc+1} {result}')