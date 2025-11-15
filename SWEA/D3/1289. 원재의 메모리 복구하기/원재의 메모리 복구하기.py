T = int(input())

for t in range(T):
    s = input()
    prev = "0"
    result = 0
    for ch in s:
        if ch != prev:
            result += 1
            prev = ch
    print(f"#{t + 1} {result}")