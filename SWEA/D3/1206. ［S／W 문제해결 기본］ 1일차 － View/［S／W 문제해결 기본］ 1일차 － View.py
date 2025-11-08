for t in range(10):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    for i in range(2, N - 2):
        max_height = max(arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2])
        if max_height < arr[i]:
            answer += arr[i] - max_height
    print(f"#{t + 1} {answer}")