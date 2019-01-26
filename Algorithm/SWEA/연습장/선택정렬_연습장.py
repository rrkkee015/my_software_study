def countingSort(li,k):
    for i in range(0,k):
        minIndex=i
        for j in range(i+1, len(li)):
            if li[minIndex]>li[j]:
                minIndex=j
        li[i],li[minIndex]=li[minIndex],li[i]
    return li

li=[6,1,7,2,3,4]
print(countingSort(li,3))
print(countingSort(li,5))