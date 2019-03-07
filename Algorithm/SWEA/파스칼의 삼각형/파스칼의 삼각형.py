import sys
sys.stdin=open('input.txt','r')

testcases=int(input())
for tc in range(testcases):
    N=int(input())
    for i in range(N):
        for j in range(0,i+1):
# testcases=int(input())
#
# def pascal(lis):
#     global cnt
#     cnt+=1
#     result='1 '
#     if cnt==N:
#         return
#     else:
#         for _ in range(1,len(lis)):
#             result+=str(lis[_-1]+lis[_])+' '
#         result+='1'
#     print(result)
#     lis=list(map(int,result.split()))
#     pascal(lis)
#
# for tc in range(testcases):
#     N=int(input())
#     cnt=0
#     print('#{}'.format(tc+1))
#     print(1)
#     pascal([1])