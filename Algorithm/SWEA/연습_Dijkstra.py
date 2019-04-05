route = [1, 2, 3, 1, 3, 4, 3, 2, 1, 2, 4, 5, 3, 4, 4, 3, 5, 5, 5, 1, 3, 4, 5, 3, 4, 6, 4, 5, 6, 5]
mat = [[0xfffff] * 7 for _ in range(7)]

for _ in range(0, len(route), 3):
    mat[route[_]][route[_ + 1]] = route[_ + 2]

U = [1]
D = [0] * 7
V = [_ for _ in range(1, 7)]
# 처음 애는 달래줘서 처음부터 넣어야 함
for _ in range(7):
    D[_] = mat[1][_]
w = 1

while U != V:
    for _ in range(len(mat[w])):
        if mat[U[w]][_] == min(mat[U[w]]):
            w = _
            break
    U.append(w)
    for _ in range(len(mat[w])):
        if mat[w][_] < 0Xfffff:
            D[_] = min(D[_], D[w] + mat[w][_])
    print(D)

# 포기