import sys
sys.stdin = open('input.txt','r')

for tc in range(10):
    tc = int(input())
    mat = []
    for i in range(100): # 패딩을 넣고 하면 인덱스를 생각할 필요가 없어서 편하다
        temp = list(map(int,input().split()))
        temp.insert(0,0)
        temp.append(0)
        mat.append(temp)
    for j in range(100):
        if mat[99][j] == 2:
            g = j
    for i in range(99, -1, -1):
        if mat[i][g - 1] == 1:
            while mat[i][g - 1] == 1:
                g -= 1
        elif mat[i][g + 1] == 1:
            while mat[i][g + 1] == 1:
                g += 1
    print('#{} {}'.format(tc, g - 1))