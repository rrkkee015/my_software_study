#2차원 리스트를 1차원 리스트로 만들기
#입력
#[[1],[2]]
#[['A','B'],['X','Y'],['1']]
#출력
#[1,2]
#['A','B','X','Y','1']
def solution(mylist):
    answer=[]
    for i in mylist:
        for j in i:
            answer.append(j)
    return answer

