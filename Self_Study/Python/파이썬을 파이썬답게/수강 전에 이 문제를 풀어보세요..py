#정수를 담은 이차원 리스트, mylist가 solution 함수의 파라미터로 주어집니다.
#solution 함수가 mylist 각 원소의 길이를 담은 리스트를 리턴하도록 코드를 작성해주세요.

#입력 :
#[[1],[2]]
#출력 :
#[1, 1]
#입력 :
#[[1,2],[3,4],[5]]
#출력 :
#[2,2,1]

def solution(mylist):
    for i in mylist:
        mylist[mylist.index(i)]=len(i)
    return mylist
