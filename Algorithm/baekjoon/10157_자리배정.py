Y,X=list(map(int,input().split()))
seats=[[0]*X for _ in range(Y)]
seat=int(input())
dxdy=[(-1,0),(0,-1),(1,0),(0,1)]
direct=-1
S=[0,0]
cnt=1
BP=True
while BP:
    if cnt == seat:
        print(S[0] + 1, S[1] + 1)
        break
    if direct==-5:
        direct=-1
    if 0<=S[0]+dxdy[direct][0]<Y and 0<=S[1]+dxdy[direct][1]<X and seats[S[0]+dxdy[direct][0]][S[1]+dxdy[direct][1]]==0:
        seats[S[0]][S[1]] = cnt
        cnt += 1
        S[0]+=dxdy[direct][0]
        S[1]+=dxdy[direct][1]
    else:
        direct -= 1
    if cnt==Y*X:
        BP=False
        seats[S[0]][S[1]]=cnt
for i in seats:
    print(i)
if seat>cnt: #만약 전 좌석에서 대기번호 다 찼으면 0 출력해라고 나와있음
    print(0)
