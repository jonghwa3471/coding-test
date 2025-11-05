T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        sum_ = 0
        for j in range(N):
            if arr[i][j] == 1:
                sum_ += 1
            else:
                if sum_ == K:
                    count += 1
                sum_ = 0
        if sum_ == K:
            count += 1
                
    for i in range(N):
        sum_ = 0
        for j in range(N):
            if arr[j][i] == 1:
                sum_ += 1
            else:
                if sum_ == K:
                    count += 1
                sum_ = 0
        if sum_ == K:
            count += 1
    print(f"#{t + 1} {count}")