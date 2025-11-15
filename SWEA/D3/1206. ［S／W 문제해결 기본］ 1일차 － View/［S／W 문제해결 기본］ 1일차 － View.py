for t in range(10):
    N = int(input())
    heights = list(map(int, input().split()))
    result = 0
    for i in range(2, N - 2):
        nearby = [heights[i - 2], heights[i - 1], heights[i + 1], heights[i + 2]]
        tallest = max(nearby)
        if heights[i] > tallest:
            result += heights[i] - tallest
    print(f"#{t + 1} {result}")