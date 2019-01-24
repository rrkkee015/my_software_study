li=[6,2,5,9,1,2,5,8]

def bubble_min_to_max(li):  # 버블정렬로 작은 값에서 큰 값으로
    for i in range(len(li)-1,0,-1):  # 마지막 친구 기준 잡기
        for k in range(0, i): # 마지막 앞까지 정렬
            if li[k]>li[k+1]: # 앞에수가 크면
                li[k],li[k+1]=li[k+1],li[k] #뒤로 데리고 온다.
    return li

def bubble_max_to_min(li):
    for i in range(len(li)-1,0,-1):
        for k in range(0,i):
            if li[k]<li[k+1]: # 앞에 수가 작으면
                li[k],li[k+1]=li[k+1],li[k] # 뒤로 가지고 온다.
    return li

print(bubble_min_to_max(li))
print(bubble_max_to_min(li))