T = int(input())

for t in range(T):
    week = [0, "MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    day = input()
    d = week.index(day)
    result = 7 - d if 7 - d > 0 else 7
    print(f"#{t + 1} {result}")
    