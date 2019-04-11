def spring():
    for _ in range(N):
        for __ in range(N):
            if age_mat[_][__]:
                age_mat[_][__] = sorted(age_mat[_][__])
                dead = 0
                for ___ in range(len(age_mat[_][__])):
                    if food_mat[_][__] < age_mat[_][__][___]:
                        dead_mat[_][__].append(age_mat[_][__][___])
                        dead += 1
                    else:
                        food_mat[_][__] = food_mat[_][__] - age_mat[_][__][___]
                        age_mat[_][__][___] += 1
                for ___ in range(dead):
                    age_mat[_][__].pop()

def summer():
    for _ in range(N):
        for __ in range(N):
            while dead_mat[_][__]:
                feed = dead_mat[_][__].pop()
                food_mat[_][__] += feed // 2

def fall():
    for _ in range(N):
        for __ in range(N):
            if age_mat[_][__]:
                for ___ in age_mat[_][__]:
                    if ___ % 5 == 0:
                        for new in dxdy:
                            if not (0<=_+new[0]<N and 0<=__+new[1]<N):
                                continue
                            else:
                                age_mat[_+new[0]][__+new[1]].append(1)

def winter():
    for _ in range(N):
        for __ in range(N):
            food_mat[_][__] += robot[_][__]

N, M, K = map(int,input().split()) # 땅크기, 나무 갯수, 년 수
robot = [list(map(int,input().split())) for _ in range(N)] # 양분 배열
food_mat = [[5 for _ in range(N)] for _ in range(N)]
age_mat = [[[] for _ in range(N)] for _ in range(N)]
dead_mat = [[[] for _ in range(N)] for _ in range(N)]
dxdy = [(-1,-1),(-1,0),(-1,1),(0,1),(0,-1),(1,-1),(1,0),(1,1)]
t = 0
result = 0

for _ in range(M):
    y, x, age = map(int,input().split())
    age_mat[y-1][x-1].append(age)

while t != K:
    spring()
    summer()
    fall()
    winter()
    t += 1

for _ in range(N):
    for __ in range(N):
        if age_mat[_][__]:
            result += len(age_mat[_][__])

print(result)