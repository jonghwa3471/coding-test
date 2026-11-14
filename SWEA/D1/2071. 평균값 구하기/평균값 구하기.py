T = int(input())

for t in range(T):
    nums = list(map(int, input().split()))
    avg = sum(nums) / len(nums)
    avg = round(avg)
    print(f"#{t + 1} {avg}")