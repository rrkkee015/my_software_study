row = [0] * 8 #row[0] = 3
def isPossible(k, c): #k번째 퀸의 위치(k, c)
    # 그 이전에 결정한 퀸들의 위치, row[0 ~ k-1]
        for i in range(k):
            if k- i == abs(c - row[i]):return False
        return True

def nQueen(k, n, used):
    if k==n:
        global cnt
        cnt+=1
        return
    for i in range(n):
        if used & (1<<i): continue
        #답이 되는 선택인지 조사해서 거른다.
        row[k] = i
        nQueen(k+1, n, used | (1<<i))

cnt = 0
nQueen(0, 8, 0)