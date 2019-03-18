N=int(input())
if N==1:
    print('*')
else:
    for _ in range(N*2):
        if _%2:
            for i in range(N//2):
                print(' '+'*',end='')

        else:
            for i in range(round(N/2+0.1)):
                print('*'+' ',end='')
        print()