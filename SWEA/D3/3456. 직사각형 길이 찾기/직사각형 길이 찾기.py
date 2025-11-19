T = int(input())

for t in range(T):
    a, b, c = map(int, input().split())
    result = 0
    if a == b:
        result = c
    elif b == c:
        result = a
    else:
        result = b
    print(f"#{t + 1} {result}")