T = int(input())

for t in range(T):
    N = int(input())
    trees = list(map(int, input().split()))
    max_height = max(trees)
    total_growth = 0
    odd = 0
    for tree in trees:
        gap = max_height - tree
        total_growth += gap
        if gap % 2:
            odd += 1
    days = (total_growth // 3) * 2 + (total_growth % 3)
    one = days // 2 + days % 2
    result = 0
    if odd > one:
        result = 2 * odd - 1
    else:
        result = days
    print(f"#{t + 1} {result}")