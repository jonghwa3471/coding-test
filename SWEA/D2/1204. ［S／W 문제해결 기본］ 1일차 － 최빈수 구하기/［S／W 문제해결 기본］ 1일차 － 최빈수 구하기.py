T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    idx_arr = [0] * (len(arr) + 1)
    for num in arr:
        idx_arr[num] += 1
    max_num = max(idx_arr)
    max_idxs = [index for index, value in enumerate(idx_arr) if value == max_num]
    result = max(max_idxs)
    print(f"#{N} {result}")