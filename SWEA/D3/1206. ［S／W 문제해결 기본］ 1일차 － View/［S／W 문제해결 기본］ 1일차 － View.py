for t in range(10):
    N = int(input())
    height = list(map(int, input().split()))
    count = 0
    for i in range(2, N - 2):
        highest = max(height[i -2], height[i - 1], height[i + 1], height[i + 2])
        if height[i] > highest:
            count += height[i] - highest
    print(f"#{t + 1} {count}")