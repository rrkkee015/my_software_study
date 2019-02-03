import sys
sys.stdin=open('sample_input.txt','r')

testcases = int(input())
for tc in range(testcases):
	K,N,M=tuple(map(int,input().split()))
	roads=[0]*(N+1) #정류장 갯수만큼 0으로 된 리스트 만들기
	station=list(map(int,input().split())) 
	for i in station:
		roads[i]=1 #충전소가 있는 정류장은 1로 채우기
	bus=0
	result=0 #버스가 움직인 횟 수
	while bus < N:
		bus+=K #버스 출발
		if bus>=N:#버스가 도착점에 도달하거나 넘어버리면
			break #브레이크
		elif roads[bus]==1: #버스가 충전소에 위치하면
			result+=1
			continue #계속 운행
		else:#버스가 도착했는데 그 곳에 충전소가 아니라면?
			for i in range(K-1):#K가 되면 버스가 출발했던 지점이 되어버리니 K-1까지만
				bus-=1 #뒤로 슬금슬금
				if roads[bus]==1:#충전소를 만나면
					result+=1
					break#다시출발
			else:
				result=0 #뒤로 왔는데도 충전소가 없으면
				break #결과는 0
	print(f'#{tc+1} {result}')

