T = int(input())

for t in range(T):
    table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    S = input()
    binary = ""
    result = ""
    for s in S:
        index = table.index(s)
        binary += format(index, "06b")
    for i in range(0, len(binary), 8):
        byte = binary[i : i + 8]
        ch = chr(int(byte, 2))
        result += ch
    print(f"#{t + 1} {result}")