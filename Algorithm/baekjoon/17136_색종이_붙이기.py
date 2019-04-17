mat = []
papers = [5, 5, 5, 5, 5, 5]
sum_paper = 0
min_ = 0xffffff
for i in range(10):
    temp = list(map(int,input().split()))
    for j in temp:
        if j == 1:
            sum_paper += 1
    mat.append(temp)

def attach(i, j, cnt):
    global min_, sum_paper
    if -1 in papers:
        return
    if cnt > min_:
        return
    if sum_paper < 0:
        return
    if j == 10:
        attach(i + 1, 0, cnt)
        return
    if i == 10:
        return
    if sum_paper == 0:
        if cnt < min_:
            min_ = cnt
    else:
        if mat[i][j] == 0:
            attach(i, j + 1, cnt)
        elif mat[i][j] == 1:
            for _ in range(5, 0, - 1):
                tf = False
                if i + _ > 10 or j + _ > 10:
                    continue
                for y in range(i, i + _):
                    for x in range(j, j + _):
                        if mat[y][x] == 0:
                            tf = True
                            break
                    if tf:
                        break
                else:
                    for y in range(i, i + _):
                        for x in range(j, j + _):
                            mat[y][x] = 0
                    papers[_] -= 1
                    sum_paper -= _ ** 2
                    attach(i, j, cnt + 1)
                    for y in range(i, i + _):
                        for x in range(j, j + _):
                            mat[y][x] = 1
                    papers[_] += 1
                    sum_paper += _ ** 2

attach(0, 0, 0)
if min_ == 0xffffff:
    print(-1)
else:
    print(min_)