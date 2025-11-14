T = int(input())

for t in range(T):
    arr = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    first_month, first_day, second_month, second_day = map(int, input().split())
    day = second_day - first_day + 1
    month = 0
    for i in range(first_month, second_month):
        month += arr[i]
    result = month + day
    
    print(f"#{t + 1} {result}")