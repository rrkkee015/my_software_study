import copy


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

            result.append(copy.copy(l))
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1

    return result

l = [1, 2, 3, 4, 5]
print(permute(l))