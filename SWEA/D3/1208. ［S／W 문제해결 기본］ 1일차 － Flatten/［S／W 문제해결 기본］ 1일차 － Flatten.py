for t in range(10):
    N = int(input())
    height = list(map(int, input().split()))
    for i in range(N):
        max_height = max(height)
        min_height = min(height)
        max_index = height.index(max_height)
        min_index = height.index(min_height)
        height[max_index] -= 1
        height[min_index] += 1
    max_ = max(height)
    min_ = min(height)
    result = max_ - min_
    print(f"#{t + 1} {result}")