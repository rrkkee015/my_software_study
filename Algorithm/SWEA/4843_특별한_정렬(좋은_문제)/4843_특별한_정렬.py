# 짝수는 최댓값에서 작아지고,
# 홀수는 최솟값에서 커진다.
# 1. 처음 시작 기준 애들끼리 대소 비교한다.
# 2. 짝수(2*i)이고 홀수 뒤에 있는 리스트를 비교하면서 작은 값을 가져온다.
# 3. 홀수(2*i+1)이고 본인 뒤에 있는 리스트를 비교하면서 인덱스를 가져와 지한테 박는다.
# 4. 2,3 실행했으면 i+=1
# 5. 1번부터 다시 반복 (5번 돌리면 10개를 뽑을 수 있다.)
import sys
sys.stdin=open('sample_input.txt','r')
testcases=int(input())

def my_sort(li):
    z=0
    for i in range(5):
        maxIndex=2*z
        minIndex=2*z+1
        initial=maxIndex
        initial_2=minIndex

        if li[maxIndex]<li[minIndex]:
            li[maxIndex],li[minIndex]=li[minIndex],li[maxIndex]

        for k in range(2*(z+1),len(li)):
            if li[maxIndex]<li[k]:
                maxIndex=k
        li[initial],li[maxIndex]=li[maxIndex],li[initial]

        for j in range(2*(z+1),len(li)):
            if li[minIndex]>li[j]:
                initial=minIndex
                minIndex=j
        li[initial_2],li[minIndex]=li[minIndex],li[initial_2]

        z+=1
    return ' '.join(list(map(str,li[:10])))

for test in range(testcases):
    n=input()
    li=list(map(int,input().split()))
    print(f'#{test+1} {my_sort(li)}')