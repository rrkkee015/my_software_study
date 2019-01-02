#ord(문자) : 문자의 ASCII코드를 반환한다.
#chr(숫자) : 숫자에 대응하는 문자를 반환한다.
#ord("A")
#결과값 65
#Chr(65)
#결과값 65

#import sys #시스템 중단 함수를 부르기 위해서 먼저 import를 함
a=input("")
b=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
c=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
n=0
m=0
result=0
for i in b:
    if a == i :
        result +=1
        print(a + "(ASCII: " + str(ord(a)) + ") => " + c[n] + "(ASCII: " + str(ord(c[n])) + ")")
    n+=1
for j in c:
    if a == j:
        result+=1
        print(a + "(ASCII: " + str(ord(a)) + ") => " + b[m] + "(ASCII: " + str(ord(b[m])) + ")")
#        else:
#            print(a)
#        sys.exit() # 시스템 중단 함수를 대입 !
    m+=1
if result !=1:
    print(a)
