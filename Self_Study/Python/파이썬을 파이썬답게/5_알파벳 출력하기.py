num = int(input())
alpha = "abcdefghijklmnopqrstuvwxyz"
if num == 0:
    print(alpha)
else:
    print(alpha.upper())

#alpha 다 치기엔 너무 무식하잖아
#다른 방법이 있다
import string
string.ascii_lowercase #얘는 소문자 전체
string.ascii_uppercase #얘는 대문자 전체
string.ascii_letter #얘는 대소문자 전체
stirng.digits #얘는 숫자임

#즉 위의 코드를
import string
num = int(input())
if num == 0:
    print(string.ascii_lowercase)
else:
    print(string.ascii_uppercase)
#이래도 된다.
