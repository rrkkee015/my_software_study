# N=int(input())
# num=10
# cnt=10
# if 1<=N<=10:
#     print(N-1)
# else:
#     while True:
#         sur=True
#         num_=str(num)
#         for i in range(len(num_)-1):
#             if num_[i] > num_[i+1]:
#                 continue
#             else:
#                 sur=False
#                 num=len(str(num))
#                 break
#         if sur==True:
#             cnt+=1
#         if N==cnt:
#             print(num)
#             break
#         num += 1

def my_sort(lis): #부분 집합 한 result를 sort 하기 위한 함수
    for i in range(len(lis)-1,0,-1):
        for j in range(0,i):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
    return lis

N=int(input())
max_num='0123456789' # 얘를 뒤집으면 줄어드는 수의 최댓 값이 나온다 9876543210
n=len(max_num) # 브루트 포스를 하기 위해 길이를 구했다.
result=[]
for i in range(1<<n):
    num=''
    for j in range(n):
        if i & 1<<j:
            num+=max_num[j] #부분집합의 요소를 만든다.
    if num!='': #부분집합에 공집합도 들어가니 걔는 빼준다.
        result+=[int(num[::-1])] #작은 수 부터 부분집합이 쌓이니 걔를 뒤집고 str 형태이니까 int로 바꿔준다.

result=my_sort(result)
if N>1023: #0~1023까지 총 2의 10인 1024가지의 result가 있는데 그 인덱스를 넘어가면 N번째 줄어드는 수가 없으니 -1을 출력
    print(-1)
else:
    print(result[int(N)-1]) #0~1023의 인덱스를 가지고 있으니 result의 N-1 인덱스 값을 출력 한다.