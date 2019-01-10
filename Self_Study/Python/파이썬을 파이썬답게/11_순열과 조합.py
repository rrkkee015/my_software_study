#순열과 조합
#숫자를 담은 일차원 리스트, mylist에 대해 mylist의 원소로 이루어진 모든 순열을 사전순으로 리턴하는
#함수 solution을 완성해 주세요
#입력:
#[2, 1]
#[1, 2, 3]
#출력:
#[[1, 2], [2, 1]]
#[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
def permute(l):
    n = len(l)
    result = []
    c = n * [0]

    result.append(l)

    i = 0;
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                tmp = l[0]
                l[0] = l[i]
                l[i] = tmp

            else:

                tmp = l[c[i]]
                l[c[i]] = l[i]
                l[i] = tmp

            result.append(l)
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1

    return result

l = [1, 2, 3, 4, 5]
print(permute(l))
