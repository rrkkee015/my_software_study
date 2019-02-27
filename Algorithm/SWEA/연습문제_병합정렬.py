def merge_sort(lis):
    # 나눌게 없으면 걔 리턴
    if len(lis)<=1:
        return lis
    #1. 나누기
    #2. 나눈거 또 재귀로 나누기
    left=merge_sort(lis[:len(lis)//2])
    right=merge_sort(lis[len(lis)//2:])

    #3. 다 나눴으면 서로 비교하기
    #4. i는 왼쪽 담당, j는 오른쪽 담당, k는 전체 리스트 담당
    i,j,k=0,0,0
    #5. i와 j가 왼쪽 오른쪽 길이를 넘어버리면 안됨
    while i < len(left) and j<len(right):
        #왼쪽이 더 작으면 왼쪽거를 리스트에 넣고
        if left[i]<right[j]:
            lis[k]=left[i]
            i+=1
        #오른쪽이 더 작으면 오른쪽거를 리스트에 넣자
        else:
            lis[k]=right[j]
            j+=1
        #넣었으면 리스트의 리스트를 한칸 증가
        k+=1
    #왼쪽 정렬이 모두 끝났다면
    if i ==len(left):
        #차례대로 오른쪽거를 넣으면 됨
        while j<len(right):
            lis[k]=right[j]
            j+=1
            k+=1
    #오른쪽 정렬이 모두 끝났다면
    elif j==len(right):
        #차례대로 왼쪽거를 넣으면 됨
        while i<len(left):
            lis[k]=left[i]
            i+=1
            k+=1
    return lis

q=[69,10,30,2,16,8,31,22]
print(merge_sort(q))