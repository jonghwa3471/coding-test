for t in range(10):
    N = int(input())
    s = input()
    stack = []
    pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
    is_valid = 1
    
    for ch in s:
        if ch in '([{<':
            stack.append(ch)
        elif ch in ')]}>':
            if not stack or stack[-1] != pairs[ch]:
                is_valid = 0
                break
            stack.pop()
            
    if stack:
        is_valid = 0
    print(f"#{t + 1} {is_valid}")