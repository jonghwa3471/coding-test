for t in range(10):
    N = int(input())
    is_valid = 1
    for _ in range(N):
        node = input().split()
        parent = node[1]
        child_count = len(node) - 2
        if parent.isdigit():
            if child_count != 0:
                is_valid = 0
        else:
            if child_count == 0:
                is_valid = 0
    print(f"#{t + 1} {is_valid}")