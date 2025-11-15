T = int(input())

for t in range(T):
    A, B = map(int, input().split())
    result = 0
    for i in range(A, B + 1):
        s = str(i)
        rev = s[::-1]
        sqrt = int(i ** 0.5)
        if s != rev:
            continue
        if sqrt * sqrt != i:
            continue
        sqrt_rev = str(sqrt)[::-1]
        if str(sqrt) == sqrt_rev:
            result += 1
    print(f"#{t + 1} {result}")