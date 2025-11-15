T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    avg = sum(arr) // N
    result = 0
    for i in arr:
        if i <= avg:
            result += 1
    print(f"#{t + 1} {result}")