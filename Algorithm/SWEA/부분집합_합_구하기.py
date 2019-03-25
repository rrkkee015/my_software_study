def powerset(temp, depth):
    depth += 1
    if depth == len(arr):
        print(temp)
    else:
        powerset(temp[:], depth)
        temp[depth]=arr[depth]
        powerset(temp[:], depth)
arr = [1,2,3]
temp = [0 for _ in range(len(arr))]
powerset(temp, -1)

# for i in range(0, 1<<len(arr)):
#     temp = []
#     for j in range(0, len(arr)):
#         if i & 1<<j:
#             temp.append(arr[j])
#     if sum(temp) == 0 and temp != []:
#         print(temp)

