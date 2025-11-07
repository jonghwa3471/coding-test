T = int(input())

for t in range(T):
    N = int(input())
    result = [0] * 8
    offset = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for i in range(len(offset)):
        result[i] = N // offset[i]
        N %= offset[i]
    print(f"#{t + 1}")
    print(*result)