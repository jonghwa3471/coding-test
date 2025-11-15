T = int(input())

for t in range(T):
    N = int(input())
    result = 1
    count = set()
    while len(count) < 10:
        n = result * N
        count.update(list(str(n)))
        result += 1
    print(f"#{t + 1} {n}")