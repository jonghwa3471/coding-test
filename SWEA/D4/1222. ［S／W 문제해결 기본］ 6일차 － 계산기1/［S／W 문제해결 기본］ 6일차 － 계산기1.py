for t in range(10):
    N = int(input())
    cmd = input()
    s = ""
    stack = []
    for c in cmd:
        if c.isdigit():
            s += c
        else:
            while stack:
                s += stack.pop()
            stack.append(c)
            
    while stack:
        s += stack.pop()
            
    sum_stack = []        
    for ch in s:
            if ch.isdigit():
                sum_stack.append(int(ch))
            else:
                a = sum_stack.pop()
                b = sum_stack.pop()
                sum_stack.append(b + a)
    result = sum_stack.pop()
    print(f"#{t + 1} {result}")