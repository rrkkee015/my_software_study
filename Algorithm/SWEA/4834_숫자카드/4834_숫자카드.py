import sys
sys.stdin=open('sample_input.txt','r')
t=int(input())
for i in range(t):
    N=int(input())
    ai=list(map(int,(','.join(input())).split(',')))
    count = {}
    result ={}
    for z in ai:
        if z in count:
            count[z] += 1
        if z not in count:
            count[z] = 1
    for k,v in count.items():
        if v == max(count.values()):
            result[k]=v
    print(f'#{i+1} {max(result.keys())} {max(result.values())}')
