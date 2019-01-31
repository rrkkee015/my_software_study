import sys
sys.stdin=open('sample_input.txt','r')
testcases=int(input())
for testcase in range(testcases):
    N,K=tuple(map(int,input().split()))
    numbers=list(map(int,input().split()))
    result = ''
    for i in range(1,N+1):
        if i not in numbers:
            result += str(i) +' '
    print(f"#{testcase+1} {result}")


###### 누군지는 모르겠다
def my_int(x):
    len_x = 0
    for i in x:
        len_x += 1
    int_x = 0
    for i in range(len_x):
        int_x += (ord(x[i]) - ord('0')) * (10 ** (len_x - 1 - i))
    return int_x


for _ in range(my_int(input())):
    N, student = input().split()
    N = my_int(N)
    arr = [0 for _ in range(N + 1)]

    p_student = input().split()
    print(f'#{_ + 1}', end=' ')
    for i in p_student:
        arr[my_int(i)] = 1

    for i in range(1, N + 1):
        if not arr[i]:
            print(i, end=' ')
    print()