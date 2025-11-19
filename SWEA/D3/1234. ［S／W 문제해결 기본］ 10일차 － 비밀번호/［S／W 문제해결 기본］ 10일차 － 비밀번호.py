for t in range(10):
    N, S = input().split()
    stack = []
    for s in S:
        if len(stack) > 0 and s == stack[-1]:
            stack.pop()
        else:
            stack.append(s)
    result = "".join(stack)
    print(f"#{t + 1} {result}")