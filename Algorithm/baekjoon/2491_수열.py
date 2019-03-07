N=int(input())
numbers=list(map(int,input().split()))
i=0
result=1
le=1
while i!=N: #나 원래 풀 땐 i!=N-1로 했는데 i!=N해도 된다. i가 numbers의 인덱스인데  numbers는 N-1까지 있으니 i가 N이 되면 정지해야한다.
    j=i+1 #j는 i 바로 앞에 있는 숫자이다.
    if j<N and numbers[i]<numbers[j]: #j 역시 범위가 N이 되서는 안된다. #뒤에가 더 크면
        le+=1 #길이 하나 증가
        temp=numbers[j] #j의 값을 temp에 담고
        j+=1 #j는 한칸 더 뒤로 간다.
        while j<N and temp<=numbers[j]: #j는 N보다 작아야하고 temp와 뒤의 수가 같거나 temp가 더 작으면 while 돌린다.
            le+=1 #길이 하나 증가
            temp=numbers[j] #다시 temp 뒤로 가고
            j+=1 #j도 뒤로 #만약 temp가 j의 수보다 작아지면 while문은 끝난다.
        if result < le: #걔가 최댓값이면 result를 갱신
            result=le
        le=1
    elif j<N and numbers[i]>numbers[j]: #j 역시 범위가 N이 되서는 안된다. #뒤에가 더 작으면
        le+=1 #길이 하나 증가
        temp=numbers[j] #j의 값을 temp에 담고
        j+=1 #j는 한칸 더 뒤로 간다.
        while j<N and temp>=numbers[j]: #j는 N보다 작아야하고 temp와 뒤의 수가 같거나 temp가 더 크면 while 돌린다.
            le+=1 #길이 하나 증가
            temp=numbers[j] #다시 temp 뒤로 가고
            j+=1 #j도 뒤로 #만약 temp가 j의 수보다 커지면 while문은 끝난다.
        if result < le: #걔가 최댓값이면 result를 갱신
            result=le
        le=1
    elif j<N and numbers[i]==numbers[j]: #j 역시 범위가 N이 되서는 안된다. #뒤에와 같으면
        le+=1 #그냥 길이를 하나 더 증가시킨다.
        if result < le: #걔가 최댓값이면 result를 갱신
            result=le
    i+=1
print(result)