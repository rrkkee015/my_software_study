#  선형으로 정렬되는 효율적인 알고리즘
#  정수형으로 짜져있어야한다.
#  범위가 정해져 있어야한다.
#  집합에 각 항목이 몇 개씩 있는지 세는 작업을 한다.

def Countingsort(li):
    n=max(li)-min(li)+1
    C=[0]*n
    B=[0]*len(li)
    for i in range(len(li)):
        C[li[i]]+=1

    for i in range(len(C)-1):
        C[i+1]+=C[i]

    for i in range(len(li)-1,-1,-1):
        B[C[li[i]]-1]=li[i]
        C[li[i]]-=1

    return B

print(Countingsort([0, 4, 1, 3, 1, 2, 4, 1]))