T = int(input())

for t in range(T):
    a, b, c = map(int, input().split())
    b_new = min(b, c - 1)
    if b_new < 2:
        print(f"#{t + 1} -1")
        continue
    a_new = min(a, b_new - 1)
    result = (a - a_new) + (b - b_new)
    print(f"#{t + 1} {result}")