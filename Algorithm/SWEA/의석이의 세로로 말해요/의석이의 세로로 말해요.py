import sys
sys.stdin=open('sample_input.txt','r')

testcases=int(input())
for tc in range(testcases):
    mat=[[-1]*100 for _ in range(5)]
    result=''
    for _ in range(5):
        word=input()
        for j in range(len(word)):
            mat[_][j]=word[j]
    for j in range(100):
        for i in range(5):
            if mat[i][j]!=-1:
                result+=mat[i][j]
    print('#{} {}'.format(tc+1,result))