A=[1,0,1,1]
B=[0,1,1,2]

for _ in range(42):
    A+=[A[-1]+A[-2]]
    B+=[B[-1]+B[-2]]

K=int(input())
print(A[K],end=' ')
print(B[K])