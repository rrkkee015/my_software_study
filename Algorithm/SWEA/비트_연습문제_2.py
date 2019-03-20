str_='0F97A3'
str_='01D06079871D79F99F'
def ten_binary(num):
    binary=['0','0','0','0']
    cnt=3
    while num:
        binary[cnt]=str(num%2)
        num=num//2
        cnt-=1
    return ''.join(binary)

def binary(num):
    for _ in range(0,len(num),7):
        sum_=0
        if len(num[_:])<7:
            for i in range((len(num[_:])-1),-1,-1):
                if int(num[_+i])==1:
                    # print()
                    # print(i-len(num[_:])-1)
                    # print((i-(len(num[_:])-1)))
                    # print('----')
                    sum_+=2**(abs(i-(len(num[_:])-1)))
            print(sum_)
        else:
            for i in range(6,-1,-1):
                if int(num[_+i])==1:
                    sum_+=2**(abs(i-6))
            print(sum_, end=' ')

def six_binary(num):
    result=''
    print(num)
    for _ in num:
        if ord(_)>=65:
            temp=ord(_)-ord('A')+10
        else:
            temp=int(_)
        result+=ten_binary(temp)
    return result

# print(ten_binary(10))
_=six_binary(str_)
binary(_)