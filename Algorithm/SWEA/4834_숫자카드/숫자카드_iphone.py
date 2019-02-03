import sys
sys.stdin=open('sample_input.txt','r')

testcases=int(input())
for testcase in range(testcases):
	N=int(input())
	num=input()
	result=0
	resultnum=0
	counting=[0]*10
	for i in num:
		counting[int(i)]+=1
	for j in range(len(counting)):
		if result <=counting[j]:
			result = counting[j]
			resultnum = j
	print(f'#{testcase+1} {resultnum} {result}')
