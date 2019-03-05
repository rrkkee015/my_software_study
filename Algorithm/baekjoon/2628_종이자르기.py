X,Y=list(map(int,input().split()))
X=[0,X]
Y=[0,Y]
result=[]
N=int(input())
for _ in range(N):
    cut=list(map(int,input().split()))
    if cut[0]==0:
        Y.append(cut[1])
    else:
        X.append(cut[1])
X=sorted(X)
Y=sorted(Y)
x=[]
y=[]
for i in range(len(X)-1):
    x.append(X[i+1]-X[i])
for j in range(len(Y)-1):
    y.append(Y[j+1]-Y[j])
for i in range(len(x)):
    for j in range(len(y)):
        result.append(x[i]*y[j])
print(max(result))
