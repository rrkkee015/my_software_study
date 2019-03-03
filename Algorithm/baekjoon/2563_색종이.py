mat=[[0]*101 for _ in range(101)]
papers=int(input())
cnt=0
for paper in range(papers):
	x,y=list(map(int,input().split()))
	for i in range(10):
		for j in range(10):
			mat[i+y][j+x]=1
for i in range(101):
	for j in range(101):
		if mat[i][j]==1:
			cnt+=1
print(cnt)