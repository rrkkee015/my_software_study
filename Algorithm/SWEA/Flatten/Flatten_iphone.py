import sys
sys.stdin=open('input.txt','r')

def my_sort(lis):
	for i in range(len(lis)-1,-1,-1):
		for j in range(i):
			if lis[j]>lis[j+1]:
				lis[j],lis[j+1]=lis[j+1],lis[j]
	return lis

testcases=10
for tc in range(testcases):
	dump=int(input())
	boxes=my_sort(list(map(int,input().split())))
	for i in range(dump):
		boxes[-1]=boxes[-1]-1
		boxes[0]=boxes[0]+1
		boxes=my_sort(boxes)
		if boxes[-1]-boxes[0]==0 or boxes[-1]-boxes[0]==1:
			break
	print(f'#{tc+1} {boxes[-1]-boxes[0]}')
		
