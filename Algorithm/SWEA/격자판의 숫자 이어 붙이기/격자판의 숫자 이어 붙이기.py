import sys
sys.stdin = open('sample_input.txt','r')

def search(y,x,num):
    if len(num) == 7:
        if num not in cnt:
            cnt[num] = 1
            return
        else:
            return
    else:
        for _ in dxdy:
            if 0<= y+_[0] < 4 and 0<= x+_[1] < 4:
                search(y+_[0],x+_[1],num + str(mat[y+_[0]][x+_[1]]))
testcases = int(input())
for tc in range(testcases):
    mat = [list(map(int,input().split())) for _ in range(4)]
    cnt = {}
    visited = [[0] * 4 for _ in range(4)]
    dxdy = [(1,0),(0,1),(-1,0),(0,-1)]
    for i in range(4):
        for j in range(4):
            if visited[i][j] == 0:
                visited[i][j] = 1
                search(i,j,'')
    print('#{} {}'.format(tc+1,len(cnt)))