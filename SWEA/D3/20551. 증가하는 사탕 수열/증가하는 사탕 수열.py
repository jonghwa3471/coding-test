T = int(input())

for t in range(T):
    arr = list(map(int, input().split()))
    result = 0
    if arr[2] <= arr[1]:
        while arr[2] <= arr[1]:
            arr[1] -= 1
            if arr[1] == 0:
                result = -1
                break
            result += 1
    if arr[1] <= arr[0]:
        while arr[1] <= arr[0]:
            arr[0] -= 1
            if arr[0] == 0:
                result = -1
                break
            result += 1
    print(f"#{t + 1} {result}")