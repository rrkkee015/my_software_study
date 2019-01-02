# 다음의 결과와 같이 입력된 문자열의 문자 빈도수를 구하는 프로그램을 작성하십시오.
# 입력 abcdefgabc
# 출력 a,2
#      b,2
#      c,2
#      d,1
#      e,1
#      f,1
#      g,1

# 1. 입력을 받을 변수를 만든다.
# 2. for 문으로 하나씩 돌리면서 if ~ in ~ 문을 사용하여서 안에 있으면 count += 1 해준다.
# 3. 기존 카운트는 1이다.

let = input('')
result = []
result_dict={}

for i in let:
    count = 1
    if i in result:
        count +=1
    result.append(i)
    result_dict.update({i:count})

for key in result_dict:
    print("{},{}".format(key,result_dict[key]))
