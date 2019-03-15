N=int(input())

for _ in range(N):
    for __ in range(N):
        if _%2==0:
            print('*',end=' ')
        else:
            print(' '+'*',end='')
    print()