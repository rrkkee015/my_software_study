#정수를 담은 이차원 리스트, mylist가 solution 함수의 파라미터로 주어진다.
#solution 함수가 mylist 각 원소의 길이를 담은 리스트를 리턴하도록 빈칸을 완성해보세요
#map 함수를 활용하세요.

li1 = [[1],[2]]
li2 = [[1,2],[3,4],[5]]

print(list(map(len,li1)))
print(list(map(len,li2)))
