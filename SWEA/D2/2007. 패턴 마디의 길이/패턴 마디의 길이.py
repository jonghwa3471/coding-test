T = int(input())

for t in range(T):
    string = input()
    result = 0
    for i in range(1, 11):
        if string[: i] == string[i : i * 2]:
            result = i
            break
    print(f"#{t + 1} {result}")