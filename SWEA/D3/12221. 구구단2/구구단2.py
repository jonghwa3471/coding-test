T = int(input())

for t in range(T):
    n1, n2 = map(int, input().split())
    if n1 >= 10 or n2 >= 10:
        result = -1
    else:
        result = n1 * n2
    print(f"#{t + 1} {result}")