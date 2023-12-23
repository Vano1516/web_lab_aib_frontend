def count_routes(N, M):
    if not (1 <= N <= 50 or 1 <= M <= 50):
        print("Введены некорректные данные")
        return None
    dp = [[0] * M for z in range (N)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(M):
            if i + 2 < N and j + 1 < M:
                dp[i + 2][j + 1] += dp[i][j]
            if i + 1 < N and j + 2 < M:
                dp[i + 1][j + 2] += dp[i][j]
    return dp[N - 1][M - 1]
print("Введите количество строк N и количество столбцов M:")
N, M = map(int, input().split())
result =count_routes(N, M)
print("Количество способов добраться до правого нижнего угла: " + str(result))
