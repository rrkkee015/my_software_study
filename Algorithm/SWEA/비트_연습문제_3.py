def six_binary(num):
    result=''
    for _ in num:
        if ord(_)>=65:
            temp=ord(_)-ord('A')+10
        else:
            temp=int(_)
        result+=ten_binary(temp)
    return result

def ten_binary(num):
    binary=['0','0','0','0']
    cnt=3
    while num:
        binary[cnt]=str(num%2)
        num=num//2
        cnt-=1
    return ''.join(binary)

def find(num):
    for _ in range(len(num)):
        temp=''
        for __ in range(6):
            temp+=num[_+__]
        if temp in password:
            start=_
            break
    for _ in range(start,len(num),6):
        if len(num[_:])<6:
            return
        else:
            temp=num[_:_+6]
            for __ in range(len(password)):
                if temp==password[__]:
                    print(__,end=' ')

str_='0DEC'
str_='0269FAC9A0'
password=['001101','010011','111011','110001','100011','110111','001011','111101','011001','101111']
_=six_binary(str_)
find(_)