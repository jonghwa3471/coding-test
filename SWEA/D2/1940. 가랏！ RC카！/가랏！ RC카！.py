T = int(input())

for t in range(T):
    N = int(input())
    speed = 0
    result = 0
    for n in range(N):
        cmd = list(map(int, input().split()))
        if cmd[0] == 2:
            speed -= cmd[1]
            if speed < 0:
                speed = 0
        if cmd[0] == 1:
            speed += cmd[1]
        result += speed
    print(f"#{t + 1} {result}")