import sys
sys.stdin=open('input.txt','r')

    def making_matrix(N):
        matrix = [[0] * N for i in range(N)]
        reverse_matrix = [[0]*N for i in range(N)]
        for i in range(N): #matrix
            sentence = input()
            for j in range(len(sentence)):
                matrix[i][j]=sentence[j] #matrix
                reverse_matrix[j][i]=sentence[j] #reverse_matrix
        return matrix,reverse_matrix

    def find(matrix):
        num=0
        for sentence in matrix:
            for M in range(1,101):
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
                n=len(result)
                if n == M//2:
                    if M % 2 == 1:
                        n=n*2+1
                    else:
                        n=n*2
                if num < n:
                    num = n
        return num

for tc in range(10):
    testcase=int(input())
    N=100
    matrix,reverse_matrix=making_matrix(N)
    a = find(matrix)
    b = find(reverse_matrix)
    if a>b:
        result=a
    else:
        result=b
    print(f'#{testcase} {result}')