papers = [0, 5, 5, 5, 5, 5]
mat = []
sum_paper = 0
min_ = 0xffffff

for _ in range(10):
    temp = list(map(int,input().split()))
    for __ in temp:
        if __ == 1:
            sum_paper += 1
    mat.append(temp)

def attach(i,j,cnt):
    global sum_paper, min_
    if i == 10:
        return
    if sum_paper < 0:
        return
    if -1 in papers:
        return
    if min_ < cnt:
        return
    if sum_paper == 0:
        if min_ > cnt:
            min_ = cnt
        return
    if mat[i][j] == 0:
        if j +  1 == 10:
            attach(i + 1, 0, cnt)
        else:
            attach(i, j + 1, cnt)
    else:
        for _ in range(5,0,-1):
            tf = False
            if i + _ > 10 or j + _ > 10:
                continue
            else:
                for y in range(i, i+ _):
                    for x in range(j, j + _):
                        if mat[y][x] == 0:
                            tf = True
                            break
                    if tf:
                        break
                else:
                    for y in range(i, i+_):
                        for x in range(j, j+_):
                            mat[y][x] = 0
                    sum_paper -= _ ** 2
                    papers[_] -= 1
                    attach(i,j,cnt + 1)
                    for y in range(i, i + _):
                        for x in range(j, j + _):
                            mat[y][x] = 1
                    sum_paper += _ ** 2
                    papers[_] += 1

attach(0,0,0)
if min_ == 0xffffff:
    print(-1)
else:
    print(min_)