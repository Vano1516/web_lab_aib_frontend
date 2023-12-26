def count_routes(N, M):
    cr = [[0] * M for _ in range(N)]
    cr[0][0] = 1
    
    for i in range(N):
        for j in range(M):
            if (i >= 2 and j >= 1) or (i >= 1 and j >= 2):
                cr[i][j] = cr[i-2][j-1] + cr[i-1][j-2]
    
    return cr[N-1][M-1] 

N, M = map(int, input().split())

print(count_routes(N, M))
