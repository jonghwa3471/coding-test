T = int(input())

for t in range(T):
    S = input()
    table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    binary = ""
    result = ""
    for s in S:
        binary += format(table.index(s), "06b")
    for i in range(0, len(binary), 8):
        result += chr(int(binary[i : i + 8], 2))
    print(f"#{t + 1} {result}")