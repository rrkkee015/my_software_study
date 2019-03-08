testcases=int(input()) #테스트케이스

for tc in range(testcases):
    N, K = list(map(int,input().split())) #게임 판의 크기 N, 'X' 모양의 크기 K
    mat=[list(map(int,input().split())) for _ in range(N)] #게임판 제작
    result=1000000 #최솟값을 담을 그릇
    for i in range(0,N-K+1): #만약 N이 10이고 K가 3이라면 행렬 순회는 7까지 돌아야 하니 경계는 10-3+1이다.
        for j in range(0,N-K+1): #마찬가지
            A=0 #오른쪽 대각선
            B=0 #왼쪽 대각선
            for p in range(K): #도구 크기만큼 돌자
                for q in range(K): #도구 크기만큼 돌자
                    if p==q: #같으면 오른쪽 대각선
                        A+=mat[p+i][q+j] #오른쪽 대각선 값에 담자
                    if p+q==K-1: #왼쪽 대각선은 서로 인덱스의 합이 K-1한 값이다.
                        B+=mat[p+i][q+j]
            temp=abs(A-B) #위에서 도구 인덱스가 중요한데 시작위치인 i,j값을 각각의 값에 더해줘야한다.
            if result>temp: #temp가 최솟값이라고 불리는 애보다 작다면
                result=temp #걔를 최솟값으로 갱신해야 함
    print('#{} {}'.format(tc+1,result)) #출력