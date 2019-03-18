def password(idx,word,moum,jaum):
    global result
    if len(word)==L and moum>=1 and jaum>=2:
        result+=[word]
        return
    elif idx==C:
        return
    else:
        if ord(alphabets[idx]) in [97,101,105,111,117]:
            password(idx+1,word[:],moum,jaum)
            word.append(alphabets[idx])
            password(idx+1,word[:],moum+1,jaum)
        else:
            password(idx+1,word[:],moum,jaum)
            word.append(alphabets[idx])
            password(idx+1,word[:],moum,jaum+1)

L, C = list(map(int,input().split()))
alphabets=list(map(str,input().split()))
alphabets=sorted(alphabets)
result=[]
password(0,[],0,0) # 인덱스, word, 모음 갯수, 자음 갯수
for i in sorted(result):
    print(''.join(str(x) for x in i))
