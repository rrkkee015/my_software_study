# import  sys
# sys.stdin = open('sample_input.txt','r')
#
# testcases=int(input())
#
# for test in range(testcases):
def my_sort(lis):
    for i in range(len(lis)-1,0,-1):
        for k in range(0,i):
            if lis[k]>lis[k+1]:
                lis[k],lis[k+1]=lis[k+1],lis[k]
    return lis

def my_reverse(lis):
    new_lis=[0]*len(lis)
    for i in range(len(lis)-1,-1,-1):
        new_lis[(len(lis)-1)-i]=lis[i]
    return new_lis

def my_join(lis):
    result =''
    for i in lis:
        if not i == lis[-1]:
            result+=str(i) +' '
        else:
            result+=str(i)
    return result

# lis_len=int(input())
# li=list(map(int,input().split()))

sorted_li=my_sort(li)
reversed_li=my_reverse(sorted_li)

result=[0]*10

cnt = 0
odd = 0
even = 0

while cnt != 10:
    cnt+=1
    if  cnt % 2:
        result[cnt-1]=reversed_li[odd]
        odd+=1
    else:
        result[cnt-1]=sorted_li[even]
        even+=1
print(result)

    # print(f'#{test+1} {my_join(result)}')
