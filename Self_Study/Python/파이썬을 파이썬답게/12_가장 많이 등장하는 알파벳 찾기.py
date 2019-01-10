#이 문제에는 표준 입력으로 문자열, mystr이 주어집니다.
#mystr에서 가장 많이 등장하는 알파벳만을 사전 순으로 출력하는 코드를 작성해주세요.
#입력:
#'aab'
#'dfdefdgf'
#출력:
#'a'
#'df'
def my_str(my):
    result=[]
    count=1
    for i in my:
        if my.count(i) > count:
            count = my.count(i)
        result += list(i)
    for j in result[:]:
        if count > result.count(j):
            result.remove(j)
    return ''.join(sorted(list(set(result))))
my=input('')
print(my_str(my))
