#정수를 담은 리스트 mylist를 입력받아, 이 리스트의 원소 중 짝수인 값만을 제곱해 담은 새 리스트를 리턴하는
#solution 함수를 완성해주세요. 예를 들어 [3,2,6,7]이 주어진 경우 [4, 36]을 리턴해야합니다.

def solution(mylist):
    answer=[]
    for i in mylist:
        if i % 2 ==0:
            answer.append(i**2)
    return answer
