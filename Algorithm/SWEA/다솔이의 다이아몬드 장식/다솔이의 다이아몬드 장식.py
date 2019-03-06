import sys
sys.stdin=open('sample_input.txt','r')

testcases=int(input())

for tc in range(testcases):
    word=input()
    mat=[[0]*(len(word)*4+1) for _ in range(5)]
    wordcnt=0
    for i in range(5):
        w = 0
        x = 0
        y = 0
        z = 0
        for j in range(len(mat[0])):
            if i==0 or i==4:
                if j==(4*y+2):
                    y+=1
                    mat[i][j]='#'
                else:
                    mat[i][j]='.'
            elif i==1 or i==3:
                if j==(2*x+1):
                    x+=1
                    mat[i][j]='#'
                else:
                    mat[i][j]='.'
            else:
                if j==4*z+2:
                    z+=1
                    mat[i][j]=word[wordcnt]
                    wordcnt+=1
                elif j==4*w:
                    w+=1
                    mat[i][j]='#'
                else:
                    mat[i][j]='.'
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j],end='')
        print()