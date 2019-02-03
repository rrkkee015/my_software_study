testcases=int(input())
for tc in range(testcases):
    nums=input()
    for i in range(1<<len(nums)):
        result=''
        for j in range(len(nums)):
            if i & 1<<j:
                result += nums[j]
        print(result)