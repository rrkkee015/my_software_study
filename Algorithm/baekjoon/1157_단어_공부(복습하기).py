#알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하세요.
#단, 대문자와 소문자를 구분하지 않습니다.
#입력:
#첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
#출력:
#첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우 ?를 출력

a=input().upper()
dic={}
result=[]
for i in a:
    if i in dic:
        dic[i]+=1
    if i not in dic:
        dic[i]=1
result=[k for k,j in dic.items() if j == max(dic.values())]
print('?' if len(result) >=2 else result[0])

import sys
input=sys.stdin.readline
a=input().upper()
c=0
r=[]
for i in a:
    if a.count(i)>=c:
        c=a.count(i)
        r.append(i)
r.pop()
print('?' if len(set(r)) >= 2 else r[0])

#다른 사람 코드
s=input().upper()
a={x:0 for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
for i in a.keys():
    a[i]+= s.count(i)
l=sorted(a.values())
m=max(l)
print(l)
if m==l[-2]:
    c="?"
else:
    for k, v in a.items():
        if v==m:
            c=k
print(c)
