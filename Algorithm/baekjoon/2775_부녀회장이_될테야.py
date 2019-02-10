first=[i for i in range(1, 15)]
result=[[0 for i in range(14)] for k in range(15)]
for k in range(14):
    result[0][k]=first[k]
for i in range(1,15):
    for k in range(14):
        result[i][k]=sum(result[i-1][:k+1])
testcases=int(input())
for tc in range(testcases):
    k=int(input())
    n=int(input())
    print(result[k][n-1])