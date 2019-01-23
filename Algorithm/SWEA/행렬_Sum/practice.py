import sys

sys.stdin=open('input.txt','r')
testcases=10
li=[]
for test in range(testcases):
    t = int(input())
    for i in range(100):
        li2=list(map(int,input().split()))
        li.append(li2)
print(li)