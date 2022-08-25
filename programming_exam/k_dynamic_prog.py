def main():
    symbol2number = {'.': 0, '#': 1}

    n, m = map(int, input().split())
    array = [list(map(lambda v: symbol2number[v], list(input()))) for _ in range(n)]

    dp = [[] for _ in range(n)]
    dp[0].append(array[0][0])

    for i in range(n):
        for j in range(m):
            if i - 1 < 0 and j - 1 < 0:
                continue
            elif i == 0:
                add = array[i][j] if array[i][j - 1] == 0 and array[i][j] == 1 else 0
                dp[i].append(dp[i][j - 1] + add)
            elif j == 0:
                add = array[i][j] if array[i - 1][j] == 0 and array[i][j] == 1 else 0
                dp[i].append(dp[i - 1][j] + add)
            else:
                if array[i][j] == 1:
                    add = array[i][j] if array[i - 1][j] == 0 else 0
                    value_top = dp[i - 1][j] + add

                    add = array[i][j] if array[i][j - 1] == 0 else 0
                    value_left = dp[i][j - 1] + add
                else:
                    value_top, value_left = dp[i - 1][j], dp[i][j - 1]

                dp[i].append(min(value_top, value_left))

    print(dp[n - 1][m - 1])


main()
