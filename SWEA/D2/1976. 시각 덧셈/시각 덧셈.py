T = int(input())

for t in range(T):
    first_hour, first_min, second_hour, second_min = map(int, input().split())
    hour = (first_hour + second_hour) % 12
    min = (first_min + second_min) % 60
    if first_min + second_min > 60:
        hour += 1
    print(f"#{t + 1} {hour} {min}")