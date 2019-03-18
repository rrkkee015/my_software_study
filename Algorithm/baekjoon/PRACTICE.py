# 정비소 방문 체크 리스트, 몇 번째 정비소 방문하고 넘겨준건지, 지금까지 정비 시간, 방문정비소 개수
def search_min(result, k,time, ccnt):
    global max_d, min_t, cnt, ans, count
    ssum = 0
    if k == 0 and result[0] == 0:
        ssum += dist[0]
    while k <= cnt-1:
        k += 1
        ssum += dist[k]
        if min_t < time:
            return
        elif ssum > max_d:
            k -= 1
            result[k] = 1
            time += hour[k]
            ccnt += 1
            return search_min(result, k, time, ccnt)
        elif k == cnt:
            if min_t > time:
                min_t = time
                ans = result
                count = ccnt
                return
        elif ssum == max_d:
            result[k] = 1
            time += hour[k]
            ccnt += 1
            return search_min(result, k, time, ccnt)

# 정비를 받지 않고 갈 수 있는 최대 거리
max_d = int(input())
# 정비소 개수는 100개 이하
cnt = int(input())
#  인접한 정비소 사이의 거리, 개수는 cnt + 1
dist = list(map(int, input().split()))
# 정비소별 정비 시간
hour = list(map(int, input().split()))

min_t = int(1e9)
count = 0
# 방문하는 정비소 번호를 담을 것
ans = 0
for i in range(2):
    # 첫 정비소를 방문할 수도 있고 안할 수도 있고
    result = [0 for i in range(cnt)]
    time = 0
    if i== 1:
        time += hour[0]
        result[0] = i
    # 방문 정비소 체크 리스트, k번째 정비소를 확인했음, 지금까지 정비 시간넘겨줌, 방문 정비소 개수
    search_min(result, 0, time, i)

# 전혀 방문하지 않아도 되는 경우 총 정비 시간은 0이고 정비소 번호는 출력X
if count == 0:
    print(0)
    print(0)
else:
    # 출력, 정비소에서 정비하는데 걸리는 총 정비 시간
    print(min_t)
    # 방문하는 정비소의 개수
    print(count)
    # 방문하는 정비소의 번호를 한 줄에 출력
    for i in range(cnt):
        if ans[i] == 1:
            print(i+1, end = ' ')