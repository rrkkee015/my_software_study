import sys
sys.stdin=open('sample_input.txt','r')
testcases=int(input())
for tc in range(testcases):
    text=input()
    sentence=input()
    M=len(text)
    N=len(sentence)
    i=0
    j=0
    while M>i and N>j:
        if text[i] != sentence[j]:
            j=j-i
            i=-1
        i+=1
        j+=1
    if M==i:
        print(1)
    else:
        print(0)