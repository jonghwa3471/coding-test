for i in range(10):
    t = int(input())
    N, M = map(int, input().split())
    result = int(N ** M)
    print(f"#{t} {result}")