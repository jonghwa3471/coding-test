T = int(input())

for t in range(T):
    N = int(input())
    result = 0
    for i in range(1, N + 1):
        if i % 2 == 0:
            result -= i
        else:
            result += i
    print(f"#{t + 1} {result}")