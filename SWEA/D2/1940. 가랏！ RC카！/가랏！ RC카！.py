T = int(input())

for t in range(T):
    N = int(input())
    current_speed = 0
    result = 0
    for i in range(N):
        command = list(map(int, input().split()))
        if len(command) != 1:
            control, speed = command[0], command[1]
            if control == 1:
                current_speed += speed
            else:
                current_speed -= speed
                if current_speed < 0:
                    current_speed = 0
        result += current_speed
    print(f"#{t + 1} {result}")