import sys
sys.stdin=open('input.txt','r')

def my_sort(lis):
	for i in range(len(lis)-1,-1,-1):
		for j in range(0,i):
			if lis[j]>lis[j+1]:
				lis[j],lis[j+1]=lis[j+1],lis[j]
	return lis

testcases=10
for tc in range(testcases):
	buildings=int(input())
	height=list(map(int,input().split()))
	result=0
	for i in range(2,buildings-2):
		high=height[i]
		lis=my_sort(height[i-2:i+3])
		if high==lis[-1]:
			result+=lis[-1]-lis[-2]
	print(f'#{tc+1} {result}')
		
