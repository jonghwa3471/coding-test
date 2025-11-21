for t in range(10):
    N = int(input())
    S = input()
    F = ""
    num_stack = []
    op_stack = []
    for s in S:
        if s.isdigit():
            F += s
        else:
            if s == "+":
                while op_stack:
                    F += op_stack.pop()
                op_stack.append(s)
            elif s == "*":
                while op_stack and op_stack[-1] == "*":
                    F += op_stack.pop()
                op_stack.append(s)
        
    while op_stack:
        F += op_stack.pop()
            
    nums = []
    op = []
    for f in F:
        if f.isdigit():
            nums.append(int(f))
        else:
            a = nums.pop()
            b = nums.pop()
            if f == "+":
                nums.append(b + a)
            elif f == "*":
                nums.append(b * a)
    result = nums.pop()
    print(f"#{t + 1} {result}")