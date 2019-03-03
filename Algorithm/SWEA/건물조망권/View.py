import sys
sys.stdin=open('input.txt','r')

def my_max(lis):
    result=-1
    for __ in lis:
        if result<__:
            result=__
    return result

for _ in range(10):
    tc=int(input())
    buildings=list(map(int,input().split()))
    result=0
    for i in range(2,len(buildings)-2):
        lis=[buildings[i-2],buildings[i-1],buildings[i+1],buildings[i+2]]
        temp=my_max(lis)
        if buildings[i]>temp:
            result+=buildings[i]-temp
    print(f'#{_+1} {result}')