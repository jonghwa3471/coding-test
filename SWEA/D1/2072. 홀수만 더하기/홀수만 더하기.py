T = int(input())

for t in range(T):
    nums = map(int, input().split())
    result = 0
    for n in nums:
        if not n % 2 == 0:
            result += n
    print(f"#{t + 1} {result}")