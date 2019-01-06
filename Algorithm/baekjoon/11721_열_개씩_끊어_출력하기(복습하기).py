#알파벳 소문자와 대문자로만 이루어진 길이가 N인 단어가 주어진다.
#한 줄에 10글자씩 끊어서 출력하는 프로그램을 작성하시오.

N=input()
s=10
l=len(N)
a=0
i=1
while l>10:
    print(N[a*s:s*i])
    a+=1
    i+=1
    l -=10
print(N[a*s:])
