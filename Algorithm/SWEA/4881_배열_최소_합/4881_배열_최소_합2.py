import sys
sys.stdin=open('sample_input.txt','r')

def mat_min_sum(depth,num,visited):
    global min_
    depth+=1
    if depth==len(mat) and min_ > num:
        min_=num
        return
    else:
        for _ in range(len(mat)):
            if visited[_]==False:
                new_visited=visited[:]
                new_visited[_]=True
                new_num=num+mat[depth][_]
                if new_num > min_ :
                    continue
                else:
                    mat_min_sum(depth,new_num,new_visited)

testcases=int(input())

for tc in range(testcases):
    N=int(input())
    mat=[list(map(int,input().split())) for _ in range(N)]
    result=[]
    min_=1000000000000000
    mat_min_sum(-1,0,[False]*N)
    print(f'#{tc+1} {min_}')