for t in range(10):
    N = int(input())
    arr = list(map(int, input().split()))
    count = 0
    for i in range(2, N - 2):
        max_height = max(arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2])
        if arr[i] > max_height:
            count += arr[i] - max_height
    print(f"#{t + 1} {count}")