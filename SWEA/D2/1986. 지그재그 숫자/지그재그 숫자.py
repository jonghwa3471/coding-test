T = int(input())
for t in range(T):
    N = int(input())
    arr = [*range(1, N + 1)]
    result = 0
    for n in arr:
        if n % 2 == 0:
            result -= n
        else:
            result += n
    print(f"#{t + 1} {result}")