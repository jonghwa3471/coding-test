T = int(input())

for t in range(T):
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N > M:
        N, M = M, N
        A, B = B, A
    result = 0
    for i in range(M - N + 1):
        sum_ = 0
        for j in range(N):
            sum_ += A[j] * B[j + i]
        if sum_ > result:
            result = sum_
    print(f"#{t + 1} {result}")