#다음을 만족하는 함수, solution을 완성해주세요.
#solution 함수는 이차원 리스트, mylist를 인자로 받습니다.
#solution 함수는 mylist 원소의 행과 열을 뒤집은 한 값을 리턴해야합니다.
#예를 들어 myplist[[1,2,3],[4,5,6],[7,8,9]]가 주어진 경우, solution 함수는
#[[1,4,7],[2,5,8],[3,6,9]] 을 리턴하면 됩니다.

#제한조건
#mylist의 원소의 길이는 모두 같다.
#mylist의 길이는 mylist[0]의 길이와 같다.
#각 리스트의 길이는 100 이하인 자연수이다.

mylist = [[1,2,3],[4,5,6],[7,8,9]]
newlist = [[],[],[]]
for i in range(0,3):
    for j in range(0,3):
        newlist[i].append(mylist[j][i])
print(newlist)

mylist1=[[0,3,1,2],[1,1,3,4],[0,3,1,3],[3,0,3,1]]
newlist2=[[],[],[],[]]
for i in range(0,4):
    for j in range(0,4):
        newlist2[i].append(mylist1[j][i])
print(newlist2)

#이렇게 해도 되지만 더 간단한 방법이 있다면?
li=[[1,2,3],[4,5,6],[7,8,9]]
print(list(map(list,zip(*li))))
#결과
#[[1,4,7],[2,5,8],[3,6,9]]

