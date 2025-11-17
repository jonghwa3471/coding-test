T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    total = [*range(1, N + 1)]
    filtered = [student for student in total if not student in arr]
    filtered.sort()
    print(f"#{t + 1}", *filtered)