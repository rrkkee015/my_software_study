import sys
sys.stdin=open('sample_input.txt','r')
testcases=int(input())

def making_matrix(N):
    matrix = [[0] * N for i in range(N)]
    reverse_matrix = [[0]*N for i in range(N)]
    for i in range(N): #matrix
        sentence = input()
        for j in range(len(sentence)):
            matrix[i][j]=sentence[j] #matrix
            reverse_matrix[j][i]=sentence[j] #reverse_matrix
    return matrix,reverse_matrix

def find(M,matrix):
    for sentence in matrix:
        cnt=0
        result = ''
        while cnt+M-1 !=N and len(result) != M//2:
            for k in range(0,M//2):
                if sentence[cnt+k] != sentence[cnt+M-1-k]:
                    result=''
                    break
                else:
                    result += sentence[k+cnt]
            cnt+=1
        if len(result) == M//2:
            if M % 2 == 1:
                result += sentence[M // 2+cnt-1] #이거 cnt라고해서 틀렸다.
            real=result
            for i in range(M//2-1,-1,-1):
                real+=result[i]
            return real

for testcase in range(testcases):
    N,M=tuple(map(int,input().split()))
    matrix,reverse_matrix=making_matrix(N)
    result = find(M,matrix)
    if result == None:
         result = find(M,reverse_matrix)
    print(f'#{testcase+1} {result}')