def lower_bound(array: list, sought: int, count: int) -> int:
    """
    Поиск наиболее близкого значения к искомому.
    Если таких несколько, то меньшее из них.

    :param array: отсортированный массив
    :param sought: искомое значение
    :param count: количество элементов (т.к. дано при вводе)

    :return: индекс ближайшего (меньшего) значения
    """

    left = 0
    right = count

    while left < right - 1:
        middle = (left + right) // 2

        if sought <= array[middle]:
            right = middle
        else:
            left = middle

    if right < count:
        dist_left, dist_right = sought - array[left], array[right] - sought

        if dist_left < dist_right:
            return left
        else:
            return right

    return left


def get_max_cnk(array, n):
    array = sorted(array)
    max_n = array[-1]
    ideal_k = max_n / 2

    index_k = lower_bound(array, ideal_k, n)

    k = array[index_k]

    print(max_n, k)


n = int(input())
array = [int(number) for number in input().split()]

get_max_cnk(array, n)
