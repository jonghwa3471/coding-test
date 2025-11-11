T = int(input())

for t in range(T):
    N = int(input())
    arr = []
    result = 0
    for n in range(N):
        row = list(map(int, list(input())))
        arr.append(row)
    for i in range(N):
        mid = N // 2
        start = abs(mid - i)
        piece = arr[i][start : N - start]
        result += sum(piece)
    print(f"#{t + 1} {result}")