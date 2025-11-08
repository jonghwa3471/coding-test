T = int(input())

for t in range(T):
    N = int(input())
    arr = set()
    k = 1
    while len(arr) < 10:
        n = N * k
        arr.update(str(n))
        k += 1
    print(f"#{t + 1} {n}")