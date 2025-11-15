T = int(input())

for t in range(T):
    N = int(input())
    print(f"#{t + 1}", end = " ")
    for i in range(1, N + 1):
        print(f"1/{N}", end = " ")
    print()