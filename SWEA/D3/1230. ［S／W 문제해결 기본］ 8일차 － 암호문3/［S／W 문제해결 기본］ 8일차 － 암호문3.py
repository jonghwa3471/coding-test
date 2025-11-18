for t in range(10):
    N = int(input())
    raw = list(map(int, input().split()))
    M = int(input())
    cmd = input().split()
    i = 0
    while i < len(cmd):
        cmd_type = cmd[i]
        if cmd_type == "I":
            x = int(cmd[i + 1])
            y = int(cmd[i + 2])
            s = list(map(int, cmd[i + 3 : i + 3 + y]))
            for index, num in enumerate(s):
                raw.insert(x + index, num)
            i += 3 + y
        elif cmd_type == "D":
            x = int(cmd[i + 1])
            y = int(cmd[i + 2])
            del raw[x : x + y]
            i += 3
        elif cmd_type == "A":
            y = int(cmd[i + 1])
            s = list(map(int, cmd[i + 2 : i + 2 + y]))
            for num in s:
                raw.append(num)
            i += 2 + y
    result = raw[0: 10]
    print(f"#{t + 1}", *result)