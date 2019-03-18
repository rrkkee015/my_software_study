def backtrack(a, k, inpu):
    global MAX
    global cnt
    cnt+=1
    result = []
    c=[0]*MAX
    inp = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    if k==inpu:
        for i in range(11):
            if a[i] == True:
                result += [i]
        if sum(result) == 10:
            print(result)
    else:
        k+=1
        ncandidates = construct_candidates(a , k, inpu, c)
        for i in range(ncandidates):
            print(a)
            a[k]=c[i]
            backtrack(a, k, inpu)

def construct_candidates(a, k, inpu, c):
    c[0]=True
    c[1]=False
    return 2

MAX=100
a=[0]*MAX
cnt=0
print(backtrack(a,0,10))
print(cnt)