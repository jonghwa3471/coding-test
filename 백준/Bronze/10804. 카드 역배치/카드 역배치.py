arr = [*range(1, 21)]

for _ in range(10):
    start, end = map(int, input().split())
    selected = arr[start - 1 : end]
    selected.reverse()
    arr[start - 1 : end] = selected

for n in arr:
    print(n, end = " ")