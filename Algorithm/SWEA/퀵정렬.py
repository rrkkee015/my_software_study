def partition(lis, p, r): # lis : 파티션을 구분할 리스트, 배열의 시작점, 배열의 끝지점
    x = lis[r] # lis의 제일 끝 지점
    i = p - 1 # 배열 처음에서 -1
    for j in range(p, r): # 배열의 시작점부터 끝 지점 앞에까지 왜냐면 x를 잡고 후두려 패는 거니까
        if lis[j] <= x: # 배열의 끝지점인 x가 순회하는 값 lis[j]보다 크면
            i+=1 # i도 j 따라서 같이 증가
            lis[i], lis[j] = lis[j], lis[i] # 서로 교환 만약에 정렬된 배열이었으면 파티션이 안나눠지고 계속 제자리에서 스위칭했겠지
                                            # 만약 x보다 큰 값이 나오면 j만 증가한다.
    lis[i+1], lis[r] = lis[r], lis[i+1] # 파티션이 들어갈 위치를 정했으니 i+1 위치와 r의 위치를 바꾸고
    return i + 1 # 새로운 pivot 값이 탄생한다.

def quicksort(lis, s, g): # lis : 정렬할 배열, s : 배열의 시작점, g : 배열의 끝 지점
    if s < g: # 시작점과 끝 점이 같을 땐, 배열 하나만 제자리에서 바꾸는 거니까 거기가 마지막임 # 왜 '<' 이거냐면 마지막 진짜 마지막에 pivot이 1로 들어온다면 두 번째 호출에서 p+1 = 2, g = 1 이 되어버려서 역전되는 경우가 있다.
        p = partition(lis, s, g) # 중간 파티션을 나누고
        quicksort(lis, s, p-1) # 피봇 기준 왼쪽
        quicksort(lis, p+1, g) # 피봇 기준 오른쪽

lis1 = [11,45,23,81,28,34] # ------------------------------
lis2 = [11,45,22,81,23,34,99,22,17,8] # 정렬할 친구들
lis3 = [1,1,1,1,1,0,0,0,0,0] # ------------------------------

quicksort(lis1, 0, len(lis1)-1) # sorted(lis1) 한 거랑 같다.
print(lis1)
quicksort(lis2, 0, len(lis2)-1)
print(lis2)
quicksort(lis3, 0, len(lis3)-1)
print(lis3)