N,M=list(map(int,input().split()))
board=[]
for _ in range(N):
    word=input()
    temp=[]
    for __ in word:
        temp+=[__]
    board+=[temp]
min=10000000
for i in range(N-8+1):
    for j in range(M-8+1):
        cnt1=0
        cnt2=0
        for y in range(8):
            for x in range(8):
                if y%2 == 0: #WBWBWBWB #BWBWBWBW
                    if x%2 == 0 and board[y+i][x+j]!='W':
                        cnt1+=1
                    if x%2 == 1 and board[y+i][x+j]!='B':
                        cnt1+=1
                    if x%2 == 0 and board[y+i][x+j]!='B':
                        cnt2+=1
                    if x%2 ==1 and board[y+i][x+j]!='W':
                        cnt2+=1
                elif y%2 == 1:
                    if x%2 == 0 and board[y+i][x+j]!='B':
                        cnt1+=1
                    if x%2 == 1 and board[y+i][x+j]!='W':
                        cnt1+=1
                    if x%2 == 0 and board[y+i][x+j]!='W':
                        cnt2+=1
                    if x%2 == 1 and board[y+i][x+j]!='B':
                        cnt2+=1
        if min > cnt1:
            min=cnt1
        if min > cnt2:
            min=cnt2
print(min)