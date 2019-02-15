testcases=int(input())

def slicing(txt):
    result=''
    for i in range(4):
        result+=txt[i]
    return result

def bringnum(txt):
    result=''
    for i in range(5,len(txt)):
        result+=txt[i]
    return int(result)

index=-1
stack = [0 for i in range(testcases)]
for tc in range(testcases):
    txt=input()
    cnt=0
    if txt=='top':
        if index<=-1:
            print(-1)
        else:
            print(stack[index])
    elif txt=='size':
        for i in stack:
            if i != 0:
                cnt+=1
        print(cnt)
    elif txt=='empty':
        for i in stack:
            if i !=0:
                print(0)
                break
        else:
            print(1)
    elif txt=='pop':
        if index<=-1:
            print(-1)
        else:
            print(stack[index])
            stack[index]=0
            index-=1
    elif slicing(txt)=='push':
        num=bringnum(txt)
        index+=1
        stack[index]=num