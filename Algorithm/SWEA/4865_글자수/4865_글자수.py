testcases=int(input())
for testcase in range(testcases):
    str1 = input()
    str2 =input()
    result=0
    for i in range(0,len(str1)):
        re = 0
        for j in range(0,len(str2)):
            if str1[i]==str2[j]:
                re+=1
        if result < re:
            result = re
    print(f'#{testcase+1} {result}')
