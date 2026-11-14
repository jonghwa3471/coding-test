T = int(input())
day31 = ["01", "03", "05", "07", "08", "10", "12"]
day30 = ["04", "06", "09", "11"]

for t in range(T):
    num = input()
    year = num[0:4]
    month = num[4:6]
    day = num[6:8]
    if month in day31 and 1 <= int(day) <= 31:
        print(f"#{t + 1} {year}/{month}/{day}")
    elif month in day30 and 1 <= int(day) <= 30:
        print(f"#{t + 1} {year}/{month}/{day}")
    elif month == "02" and 1 <= int(day) <= 28:
        print(f"#{t + 1} {year}/{month}/{day}")
    else:
        print(f"#{t + 1} -1")