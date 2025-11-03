T = int(input())

for t in range(T):
    arr = input().split()
    stack = []
    ok = True
    for item in arr:
        if item.isdigit():
            stack.append(int(item))
        elif item in "+-*/":
            if len(stack) < 2:
                ok = False
                break
            b, a = stack.pop(), stack.pop()
            if item == "+":
                stack.append(a + b)
            elif item == "-":
                stack.append(a - b)
            elif item == "*":
                stack.append(a * b)
            else:
                stack.append(a // b)
        elif item == ".":
            break
        else:
            ok = False
            break
    if not ok or len(stack) != 1:
        print(f"#{t + 1} error")
    else:
        result = stack.pop()
        print(f"#{t + 1} {result}")