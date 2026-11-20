T = int(input())

for t in range(T):
    memory = input()
    result = 0
    prev = "0"
    for m in memory:
        if m != prev:
            result += 1
        prev = m
    print(f"#{t + 1} {result}")