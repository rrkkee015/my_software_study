def selectionsort(depth):
    depth += 1
    if depth == len(lis):
        print(lis)
        return
    else:
        __ = depth
        for _ in range(depth+1,len(lis)):
            if lis[__] > lis[_]:
                __ = _
        temp = lis[__]
        lis[__] = lis[depth]
        lis[depth] = temp
        return selectionsort(depth)

def dongyoung(arr):
    if len(arr) == 1:
        return arr
    else:
        min_idx = arr.index(min(arr))
        return [arr.pop(min_idx)] + dongyoung(arr)

lis=[27,10,3,14,2,23]
selectionsort(-1)
lis=[27,10,3,14,2,23]
print(dongyoung(lis))
