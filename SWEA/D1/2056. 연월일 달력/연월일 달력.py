T = int(input())
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for t in range(T):
    num = input()
    year = num[:4]
    month = num[4:6]
    day = num[6:]
    if 1 <= int(month) <= 12 and 1<= int(day) <= months[int(month) - 1]:
        print(f"#{t + 1} {year}/{month}/{day}")
    else:
              print(f"#{t + 1} -1")