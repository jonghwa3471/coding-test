T = int(input())

for t in range(T):
    N = int(input())
    arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = [0, 0, 0, 0, 0, 0, 0, 0]
    
    for i in range(8):
        result[i] = N // arr[i]
        N %= arr[i]
    print(f"#{t + 1}")
    print(*result)