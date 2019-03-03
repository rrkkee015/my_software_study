A,B=list(map(str,input().split()))
resultA=-1
resultB=-1
for _ in range(len(A)):
    for __ in range(len(B)):
        if A[_]==B[__]:
            resultA=_
            resultB=__
            break
    if resultA>=0:
        break
for i in range(len(B)):
    if i==resultB:
        print(A)
    else:
        result='.'*(resultA)+B[i]+'.'*(len(A)-resultA-1)
        print(result)