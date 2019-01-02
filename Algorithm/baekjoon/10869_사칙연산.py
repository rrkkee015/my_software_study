#두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
#입력:7 3
#출력:10
#     4
#     21
#     2
#     1

a,b=list(map(int,input('').split(' ')))

print("{}\n{}\n{}\n{}\n{}".format(a+b,a-b,a*b,a//b,a%b))
