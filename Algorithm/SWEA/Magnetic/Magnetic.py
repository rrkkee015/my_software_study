import sys
sys.stdin=open('input.txt','r')

testcases=10

for tc in range(testcases):
    no=int(input())
    matrix=[list(map(int,input().split())) for j in range(100)]
    S_fall=False
    again = False
    stack=[]
    result=0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[j][i]==2 and S_fall == False:
                matrix[j][i]=0
            if matrix[j][i]==1:
                N_fall = False
                S_fall=True
                again=False
                stack+=[[1,j]]
                continue
            if matrix[j][i]==2 and again==True:
                matrix[j][i]=0
                new_S+=1
                matrix[new_S][i]=2
            if matrix[j][i]==1 and N_fall==False:
                continue
            elif matrix[j][i]==2 and again==False:
                y=j
                last_N=stack[-1][1]
                new_N=last_N+(y-last_N-1)//2
                new_S=new_N+1
                matrix[new_N][i]=1
                matrix[new_S][i]=2
                for a in range(len(stack)):
                    matrix[stack[a][1]][i]=0
                for k in range(1,len(stack)-1):
                    matrix[new_N-k][i]=1
                stack=[]
                result+=1
                again=True
                N_fall = True
    print(matrix)
