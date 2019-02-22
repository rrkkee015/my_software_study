def solve(n):
    global cnt
    cnt+=1
    print(cnt)
    if n == 1:
        return 1
    else:
        return 3**(n-2)+solve(n-1)

testcases=int(input())
for tc in range(testcases-1):
    cnt=0
    pills=int(input())
    print(solve(pills))
trash=input()