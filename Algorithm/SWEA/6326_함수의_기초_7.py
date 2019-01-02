# 1. number라는 변수가 input을 받도록하자.
# 2. number가 진행 될 때마다 -1의 값을 곱해주자.
# 3. while문 써서 number가 0이되면 멈추게하자
# 4. while문 내부에선 계속 곱하게 하자
def function():
    number=int(input())
    result=1
    for num in range(1,number+1):
        result = num*result
    return result
pac_man=function()
print(pac_man)
