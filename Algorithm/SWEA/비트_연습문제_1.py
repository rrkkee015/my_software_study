def teacher(arr):
    t=0
    for i in range(len(arr)):
        t = t*2 + int(arr[i])
        if (i+1) % 7 == 0:
            print(t, end=' ')
            t=0

def binary(num):
    for _ in range(0,len(num),7):
        sum_=0
        for i in range(6,-1,-1):
            if int(binary_num[_+i])==1:
                sum_+=2**(abs(i-6))
        if _==len(num)-7:
            print(sum_)
        else:
            print(sum_, end=' ')

binary_num='00000010001101'
binary_num='0000000111100000011000000111100110000110000111100111100111111001100111'
binary(binary_num)
teacher(binary_num)