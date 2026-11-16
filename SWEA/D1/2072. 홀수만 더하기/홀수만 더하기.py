T = int(input())

for t in range(T):
    arr = list(map(int, input().split()))
    result = 0
    for num in arr:
        if num % 2 != 0:
            result += num
    print(f"#{t + 1} {result}")