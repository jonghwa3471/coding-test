N = int(input())

arr = [str(i) for i in range(1, N + 1)]
rule = ["3", "6", "9"]
result = []
for num in arr:
    text = ""
    for n in num:
        if n in rule:
            text += "-"
    if text == "":
        result.append(num)
    else:
        result.append(text)
print(*result)