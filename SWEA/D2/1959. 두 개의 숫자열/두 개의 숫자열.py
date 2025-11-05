T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    K = 0
    result = 0
    if N < M:
        K = M - N
    else:
        K = N - M
        A, B = B, A
    for i in range(K + 1):
        sum_ = 0
        for j in range(len(A)):
            sum_ += A[j] * B[i + j]
        if sum_ >= result:
            result = sum_
    print(f"#{t + 1} {result}")