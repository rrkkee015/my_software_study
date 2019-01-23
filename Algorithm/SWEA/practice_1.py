inp = [[25,42,35,46,10],[33,45,16,8,0],[42,27,30,37,2],[16,43,30,47,33],[25,33,22,47,14]]
print(inp)
dx=[-1,1]
dy=[1,-1]

result=0 #결과값 달기 위한 result

def my_abs(a): #절댓값 구하는 함수
    if a==0:
        return a
    elif a<0:
        return -a
    else:
        return a

for i in range(len(inp)):
    for j in range(len(inp[i])): #2차원 순회
        re=0 #예비 결과
        for x in dx:#좌표의 상하를 다니는 for 문
            i_=i+x #i_값에 i+x를 하여서 다른 좌표를 들린다.
            if not 0<=i_<=4:#i_값이 행렬을 벗어나면 계산을 할 필요가 없으니 continue
                continue
            else:#i_값이 행렬에 포함되면
                re+=my_abs(inp[i][j]-inp[i_][j]) #기준값과 달라진 값의 차이의 절대값을 예비 결과에 더한다.
        for y in dy: #좌표의 좌우를 다니는 for 문
            j_=j+y
            if not 0<=j_<=4:
                continue
            else:
                re+=my_abs(inp[i][j]-inp[i][j_])
        result+=re
        i_=0
        j_=0
print(result)
