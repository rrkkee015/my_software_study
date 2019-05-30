N = int(input())
temp_solution = input()
solution = []
max_ = -0xfffffffffffffffff

for _ in temp_solution:
    if _ == '+' or _ == '-' or _ == '*':
        solution.append(_)
    else:
        solution.append(int(_))
cal = len(solution) // 2
order = [_ for _ in range(1, cal + 1)]
bi = []
result_bi = []

for i in range(1<<len(order)):
    temp = []
    for j in range(len(order)):
        if i & 1<<j:
            temp.append(order[j])
    bi.append(temp)

for _ in bi:
    if _ == []:
        result_bi.append([])
    elif len(_) == 1:
        result_bi.append(_)
    else:
        for __ in range(len(_) - 1):
            if _[__ + 1] - _[__] == 1:
                break
        else:
            result_bi.append(_)

for _ in result_bi:
    temp_list = solution[:]
    for __ in _:
        if temp_list[2*(__) - 1] == '+':
            for ___ in [0, -1, 1]:
                if ___ == 0:
                    temp_list[2 * (__) - 1] = temp_list[2 * (__) - 1 - 1] + temp_list[2 * (__) - 1 + 1]
                else:
                    temp_list[2 * (__) - 1 + ___] = -0xfffffffffffffffff
        elif temp_list[2*(__) - 1] == '*':
            for ___ in [0, -1, 1]:
                if ___ == 0:
                    temp_list[2 * (__) - 1] = temp_list[2 * (__) - 1 - 1] * temp_list[2 * (__) - 1 + 1]
                else:
                    temp_list[2 * (__) - 1 + ___] = -0xfffffffffffffffff
        elif temp_list[2*(__) - 1] == '-':
            for ___ in [0, -1, 1]:
                if ___ == 0:
                    temp_list[2*(__) - 1] = temp_list[2*(__) - 1 - 1] - temp_list[2*(__) - 1 + 1]
                else:
                    temp_list[2*(__) - 1 + ___] = -0xfffffffffffffffff
    for_result = []
    for __ in temp_list:
        if __ == -0xfffffffffffffffff:
            continue
        else:
            for_result.append(__)
    result = for_result[0]
    for __ in range(len(for_result)):
        if for_result[__] == '+':
            result += for_result[__ + 1]
        if for_result[__] == '-':
            result -= for_result[__ + 1]
        if for_result[__] == '*':
            result *= for_result[__ + 1]
    if max_ < result:
        max_ = result

print(max_)