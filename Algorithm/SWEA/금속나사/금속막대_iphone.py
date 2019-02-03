import sys
sys.stdin=open('input.txt','r')

testcases=int(input())
for tc in range(testcases):
    cnt=int(input())
    lis=list(map(int,input().split()))
    result=[lis[0],lis[1]] #처음 나사를 기준으로 삼는다.
    real_result=''
    while len(result) != len(lis): #결과가 원래 나사랑 같아지는 순간 종료
        for i in range(0,len(lis),2): #다른 나사들의 수나사와
            if lis[i]==result[-1]: #끼워넣을 암나사와 비교
                result+=[lis[i],lis[i+1]] #같다면 그 나사를 뒤에다가 꽂는다
        for j in range(1,len(lis),2): #다른 나사들의 암나사와
            if lis[j]==result[0]: #끼워넣어질 수나사와 비교
                result=[lis[j-1],lis[j]]+result #같다면 그 나사를 앞에다가 꽂는다
    for i in result:
        real_result+=str(i) + ' ' #일렬로 정렬
    print(f'#{tc+1} {real_result}') #출력