N = int(input())
rule = ("3", "6", "9")
result = []

for i in range(1, N + 1):
    num = list(str(i))
    s = ""
    for n in num:
        if n in rule:
            s += "-"
    if s:
        result.append(s)
    else:
        result.append(i)
print(*result)