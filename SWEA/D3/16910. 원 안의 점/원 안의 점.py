T = int(input())

for t in range(T):
    N = int(input())
    result = 0
    for i in range(-N, N + 1):
        for j in range(-N, N + 1):
            if i * i + j * j <= N * N:
                result += 1
    print(f"#{t + 1} {result}")