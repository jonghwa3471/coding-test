T = int(input())

for t in range(T):
    N = int(input())
    arr = []
    for i in range(N):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = arr[i - 1][j - 1] + arr[i - 1][j]
        arr.append(row)
    print(f"#{t + 1}")
    for row in arr:
        print(*row)