N = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr[int(N / 2)])