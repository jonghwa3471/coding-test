N = int(input())
arr = list(map(int, input().split()))
arr.sort()
index = N // 2
print(arr[index])