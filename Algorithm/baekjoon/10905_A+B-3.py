def sum_(a,b):
    print(a+b)
    return

testcases=int(input())

for tc in range(testcases):
    x,y=list(map(int,input().split()))
    sum_(x,y)