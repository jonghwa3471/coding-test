T = int(input())

for t in range(T):
    N = int(input())
    command = []
    current_speed = 0
    distance = 0
    for i in range(N):
        c = list(map(int, input().split()))
        command.append(c)
    for item in command:
        if len(item) == 2:
            if item[0] == 1:
                current_speed += item[1]
            elif item[0] == 2:
                current_speed -= item[1]
                if current_speed < 0:
                    current_speed = 0
        distance += current_speed
    print(f"#{t + 1} {distance}")