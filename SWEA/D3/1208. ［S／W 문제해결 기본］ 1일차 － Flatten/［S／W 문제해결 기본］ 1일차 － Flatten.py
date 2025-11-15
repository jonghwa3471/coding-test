for t in range(10):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N):
        max_ = max(arr)
        min_ = min(arr)
        max_index = arr.index(max_)
        min_index = arr.index(min_)
        arr[max_index] -= 1
        arr[min_index] += 1
    fin_max = max(arr)
    fin_min = min(arr)
    result = fin_max - fin_min
    print(f"#{t + 1} {result}")