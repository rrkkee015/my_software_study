# def happy_new_year(first,cnt):
#     cnt+=1
#     for _ in range(len(first)):
#         first[_]+=1
#         if first[_]>newspace[_]:
#             first[_]=1
#     if first==newyear:
#         print(cnt)
#         return
#     else:
#         happy_new_year(first,cnt)
# depth 에러 난다.
# while 문으로 바꿔보자
newyear=list(map(int,input().split()))
start=[0,0,0]
cnt=0
newspace=[15,28,19]
# happy_new_year(start,0)
while True:
    cnt+=1
    for _ in range(len(start)):
        start[_]+=1
        if start[_]>newspace[_]:
            start[_]=1
    if start==newyear:
        print(cnt)
        break
