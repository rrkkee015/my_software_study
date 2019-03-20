def Pibo(depth):
    depth+=1
    if depth == N:
        print(result[depth])
        return
    else:
        result.append(result[depth-1]+result[depth])
        Pibo(depth)

N=int(input())
result=[0,1]
Pibo(0)