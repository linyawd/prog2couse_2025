def max_product(n, m):
    s = str(n)
    length = len(s)
    dp = [[0] * (m + 1) for _ in range(length + 1)]

    for i in range(1, length + 1):
        dp[i][1] = int(s[:i])

    for j in range(2, m + 1):
        for i in range(j, length + 1):
            for k in range(1, i):
                dp[i][j] = max(dp[i][j], dp[k][j - 1] * int(s[k:i]))

    return dp[length][m]


def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    while idx < len(data):
        n = data[idx]
        m = int(data[idx + 1])
        idx += 2
        print(max_product(n, m))


if __name__ == "__main__":
    main()