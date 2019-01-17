import sys
sys.stdin=open('sample_input.txt','r')

testcase = int(input())

for test in range(testcase):
    k,n,m=tuple(map(int,input().split()))
    li=list(map(int,input().split()))
    s=0
    count=0
    for i in range(m-1): #부여받은 리스트 돌면서 예외사항들 체크 1.[i]역과 [i+1]역의 차이가 k보다 큰 경우
                            #2.처음 도착역이 k보다 큰 경우 #3.마지막 도착하려는 역이 k보다 큰 경우
        if li[i+1]-li[i]>k or li[0]>k or n-li[-1]>k:
            count=0
            break #바로 0이 출력되도록 한다.
    else: #위에 for문이 다 돌았음에도 불구하고 아무 일 없으면 else로 돌리자.
        for b in range(m): #마지막에 도착하면 굳이 충전할 필요가 없다.
            s+=k #버스 출발
            if s >= n: #버스가 도착지점이랑 같거나 크면 for문 멈춘다.
                break
            for z in li[::-1]: #list의 뒷 부분 부터 훑어서 내려간다. 안그러면 건너 뛴 부분을 중복해서 보게 된다.
                if s>=z:#s가 커지거나 같아지는 그 순간이 충전기가 필요한 순간
                    s=z#버스를 충전기로 옮기자
                    count+=1#충전..
                    break#다시 버스 출발을 위해 break5
    print(f'#{test+1} {count}')     
            
