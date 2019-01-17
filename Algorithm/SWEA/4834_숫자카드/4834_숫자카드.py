import sys
sys.stdin=open('sample_input.txt','r')

def my_max(li): #리스트를 받아 그 값의 max를 뽑는다.
    result=0
    for i in li:
        if result<i:
            result=i
    return result

def count_(li): #숫자를 쪼개어서 받아서 카운트를 하고 딕셔너리를 만든다.
    dic={}
    for j in li:
        if j in dic:
            dic[j] += 1
        if j not in dic:
            dic[j] =1
    return dic

def print_(result): #결과값 출력
    if len(result)>=2: #최다로 뽑힌 카드가 2장 이상이면
        li2 = [i[0] for i in result]
        return f'#{test+1} {my_max(li2)} {result[0][1]}' #그 중에서 최고를 뽑는다.
    else:
        return f'#{test+1} {result[0][0]} {result[0][1]}' #아니면 그냥 출력

testcase=int(input())
for test in range(testcase):
    N=int(input())
    ai=input()
    li=[int(i) for i in ai]
    result=[]
    dic=count_(li)
    result = [(k, v) for k,v in dic.items() if v == my_max(dic.values())] #value의 최고 값을 뽑아서 리스트로 만든다.
    print(print_(result))
