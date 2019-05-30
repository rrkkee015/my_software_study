def attach(i, j):
    global ones, papers, min_
    if -1 in width:
        return
    if min_ < papers:
        return
    if i == 10:
        return
    if ones == 0:
        if min_ > papers:
            min_ = papers
    else:
        if mat[i][j] == 0:
            if j + 1 == 10:
                attach(i + 1, 0)
            else:
                attach(i, j + 1)
        else:
            for _ in range(5, 0, -1):
                tf = False
                for p in range(i, i + _):
                    for k in range(j, j + _):
                        if 0 <= p < 10 and 0 <= k < 10 and mat[p][k] == 1:
                            continue
                        else:
                            tf = True
                            break
                    if tf:
                        break
                else:
                    for p in range(i, i + _):
                        for k in range(j, j + _):
                            if 0 <= p < 10 and 0 <= k < 10:
                                mat[p][k] = 0
                    width[_] -= 1
                    ones -= _ ** 2
                    papers += 1
                    if j + 1 == 10 and not i + 1 == 10:
                        attach(i + 1, 0)
                    else:
                        attach(i, j + 1)
                    for p in range(i, i + _):
                        for k in range(j, j + _):
                            if 0 <= p < 10 and 0 <= k < 10:
                                mat[p][k] = 1
                    width[_] += 1
                    ones += _ ** 2
                    papers -= 1


mat = []
width = [0, 5, 5, 5, 5, 5]
papers = 0
ones = 0
min_ = 0xffffff

for _ in range(10):
    temp = list(map(int,input().split()))
    for __ in temp:
        if __ == 1:
            ones += 1
    mat.append(temp)

attach(0, 0)
if min_ == 0xffffff:
    print(-1)
else:
    print(min_)
