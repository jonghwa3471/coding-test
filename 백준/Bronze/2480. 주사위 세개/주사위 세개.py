arr = [0] * 7

nums = list(map(int, input().split()))

for n in nums:
    arr[n] += 1
    
if 3 in arr:
    print(arr.index(3) * 1000 + 10000)
elif 2 in arr:
    print(arr.index(2) * 100 + 1000)
else:
    print(max(nums) * 100)