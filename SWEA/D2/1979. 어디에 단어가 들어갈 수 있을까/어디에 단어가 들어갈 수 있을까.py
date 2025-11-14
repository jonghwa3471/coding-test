T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        count = 0
        for j in range(N):
            if arr[i][j] == 1:
                count += 1
            if arr[i][j] == 0:
                if count == K:
                    result +=1
                count = 0
        if count == K:
            result += 1
            
    for i in range(N):
        count = 0
        for j in range(N):
            if arr[j][i] == 1:
                count += 1
            if arr[j][i] == 0:
                if count == K:
                    result += 1
                count = 0
        if count == K:
            result += 1
    print(f"#{t + 1} {result}")