import sys
sys.stdin=open('sample_input.txt','r')
testcases=int(input())
for testcase in range(testcases):
	N=int(input())
	a=list(map(int,input().split()))
	for i in range(len(a)-1,-1,-1):
		for j in range(0,i):
			if a[j]>a[j+1]:
				a[j],a[j+1]=a[j+1],a[j]
	result=a[-1]-a[0]
	print(f'#{testcase+1} {result}')
	
