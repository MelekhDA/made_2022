def partition(array, left, right):
    v = array[(left + right) // 2]
    i, j = left, right

    while i <= j:
        while array[i] < v:
            i += 1
        while array[j] > v:
            j -= 1

        if i >= j:
            break

        array[i], array[j] = array[j], array[i]
        i = i + 1
        j = j - 1

    return j


def k_statistic(array, left, right, k):
    if right - left < 1:
        return array[left]

    i = partition(array, left, right)

    if k <= i:
        return k_statistic(array, left, i, k)
    else:
        return k_statistic(array, i + 1, right, k)


n, m, k = map(int, input().split())
array = [int(number) for number in input().split()]

for _ in range(m):
    c, x = map(int, input().split())
    array += [x] * c

left, right, k = 0, len(array) - 1, k - 1
print(k_statistic(array, left, right, left + k))
