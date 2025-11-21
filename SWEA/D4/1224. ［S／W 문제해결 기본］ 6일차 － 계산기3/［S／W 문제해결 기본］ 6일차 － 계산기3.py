for t in range(10):
    N = int(input())
    exp = input()
    op = []
    postfix = ""
    for ch in exp:
        if ch.isdigit():
            postfix += ch
        elif ch == "(":
            op.append(ch)
        elif ch == ")":
            while op and op[-1] != "(":
                postfix += op.pop()
            op.pop()
        else:
            if ch == "+":
                while op and op[-1] != "(":
                    postfix += op.pop()
                op.append(ch)
            else:
                while op and op[-1] == "*":
                    postfix += op.pop()
                op.append(ch)
                
    while op:
        postfix += op.pop()
    
    num_stack = []
    for ch in postfix:
        if ch.isdigit():
            num_stack.append(ch)
        else:
            a = int(num_stack.pop())
            b = int(num_stack.pop())
            if ch == "*":
                num_stack.append(b * a)
            elif ch == "+":
                num_stack.append(b + a)
    result = num_stack.pop()
    print(f"#{t + 1} {result}")