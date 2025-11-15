T = int(input())

for t in range(T):
    a, b = 1, 1
    cmd = input()
    for c in cmd:
        if c == "L":
            a = a
            b = a + b
        else:
            a = a + b
            b = b
    print(f"#{t + 1} {a} {b}")