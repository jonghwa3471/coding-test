T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    length = len(arr)
    arr_with_index = [0] * (length + 1)
    for i in arr:
        arr_with_index[i] += 1
    most = max(arr_with_index)
    indexs = [index for index, value in enumerate(arr_with_index) if value == most]
    result = max(indexs)
    print(f"#{t + 1} {result}")