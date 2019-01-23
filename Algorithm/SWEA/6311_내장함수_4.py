# 1. 문자열을 받은 alphabet 변수를 만든다.
# 2. 람다식을 사용해서 A=4, B=3, C=2, D=1로하고 함수는
# 3. map은 int로 한다.

lis = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
result_list=[]
def function():
    for i in lis:
        if i == 'A':
            result_list.append(4)
        if i == 'B':
            result_list.append(3)
        if i == 'C':
            result_list.append(2)
        if i == 'D':
            result_list.append(1)
    return sum(result_list)

result=function()
print(result)

lis = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
liss = list(lis)
a=list(map(lambda x: '4' if x=='A' else ('3' if x=='B' else ('2' if x=='C' else '1' if x=='D' else 0)), lis))
result_str=list(map(int,a))
result=sum(result_str)
print(result)