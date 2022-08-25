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
                dp[i].append(dp[i][j - 1] + array[i][j])
            elif j == 0:
                dp[i].append(dp[i - 1][j] + array[i][j])
            else:
                dp[i].append(min(dp[i - 1][j], dp[i][j - 1]) + array[i][j])

    print(dp[n - 1][m - 1])


main()
