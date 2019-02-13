import sys
sys.stdin=open('sample_input.txt','r')
testcases=int(input())

def my_in(lis,x):
    for i in lis:
        if i == x:
            return True
    else:
        return False

def my_index(lis,x):
    for i in range(len(lis)):
        if lis[i]==x:
            return i

def my_max(lis):
    max_=0
    for i in lis:
        if max_<i:
            max_=i
    return max_

for tc in range(testcases):
    text=input()
    sentence=input()
    text_lis = []
    for w in text:
        if my_in(text_lis, w):
            continue
        else:
            text_lis+=[w]
    cnt_lis=[0]*len(text_lis)
    for se in range(len(sentence)):
        if my_in(text_lis,sentence[se]):
            cnt_lis[my_index(text_lis,sentence[se])]+=1
    print(f'#{tc+1} {my_max(cnt_lis)}')