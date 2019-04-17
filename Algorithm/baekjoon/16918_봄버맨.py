R, C, N = map(int,input().split())
full_bomb = ['O'*C]*R
bomb = {}
dxdy = [(0,0),(0,1),(1,0),(0,-1),(-1,0)]
for i in range(R):
    temp = list(input())
    for j in range(len(temp)):
        if temp[j] == 'O':
            bomb[(i,j)] = 1
if N % 2 == 0:
    for i in full_bomb:
        print(i)
else:
    for tc in range(N//2):
        temp_bomb = {}
        for i in range(R):
            for j in range(C):
                for _ in dxdy:
                    if bomb.get((i+_[0], j+_[1])) == 1:
                        break
                else:
                    temp_bomb[i, j] = 1
        bomb = temp_bomb
    result = [list('.'*C) for _ in range(R)]
    for _ in bomb.keys():
        result[_[0]][_[1]] = 'O'
    for _ in result:
        print(''.join(_))