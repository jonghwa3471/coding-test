T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    arr = [0] * (K + 1)
    arr[0] = 1
    for val in A:
        for i in range(K, val - 1, -1):
            arr[i] += arr[i - val]
    result = arr[K]
    print(f"#{t + 1} {result}")