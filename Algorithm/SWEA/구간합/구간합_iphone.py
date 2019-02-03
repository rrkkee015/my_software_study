import sys
sys.stdin=open('sample_input.txt','r')

def my_sum(lis):
	result = 0
	for i in lis:
		result+=i
	return result
	
testcases=int(input())
for tc in range(testcases):
	N,M=tuple(map(int,input().split()))
	lis=list(map(int,input().split()))
	cnt=0
	max_result=0
	min_result=999999999
	while M+cnt<=N:
		if max_result<my_sum(lis[cnt:cnt+M]):
			max_result=my_sum(lis[cnt:cnt+M])
		if min_result>my_sum(lis[cnt:cnt+M]):
			min_result=my_sum(lis[cnt:cnt+M])
		cnt+=1
	print(f'#{tc+1} {max_result-min_result}')
