import sys
sys.stdin= open('sample_input.txt','r')
testcases=int(input())

def special_sort(lis):
    result_lis = []
    cnt = 0
    max_index = 0
    min_index = 0
    while cnt != 5:
        result_max = -1
        result_min = 99999999
        cnt += 1
        for i in range(len(lis)):
            if lis[i] == '-':
                continue
            if result_max < lis[i]:
                result_max = lis[i]
                max_index = i
            if result_min > lis[i]:
                result_min = lis[i]
                min_index = i
        lis[max_index] = '-'
        lis[min_index] = '-'
        result_lis.append(result_max)
        result_lis.append(result_min)
    return result_lis

def my_join(lis):
    result =''
    for i in lis:
        if not i == lis[-1]:
            result+=str(i) +' '
        else:
            result+=str(i)
    return result

for test in range(testcases):
    n=int(input())
    lis=list(map(int,input().split()))
    result_lis = special_sort(lis)
    result_lis = my_join(result_lis)
    print(f'#{test+1} {result_lis}')
