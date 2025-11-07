T = int(input())

for t in range(T):
    startMonth, startDay, endMonth, endDay = map(int, input().split())
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    monthTerm = 0
    dayTerm = endDay - startDay + 1
    for i in range(startMonth, endMonth):
        monthTerm += month[i]
    result = monthTerm + dayTerm
    print(f"#{t + 1} {result}")