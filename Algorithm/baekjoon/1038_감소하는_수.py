def dec(jari):
    global N, num
    jari+=1
    tem = sorted(list(combinations(num,jari)))
    if len(tem) > N:
        print(''.join(tem[N]))
        return
    elif jari > 10:
        print(-1)
        return
    else:
        N -= len(tem)
        dec(jari)
# 재귀버전

from itertools import combinations
N = int(input())
jari = 0
num = '9876543210'
# while True:
#     jari += 1
#     tem = sorted(list(combinations(num,jari)))
#     if len(tem) > N:
#         print(''.join(tem[N]))
#         break
#     elif jari > 10:
#         print(-1)
#         break
#     else:
#         N -= len(tem)
# 반복문 버전
dec(0)