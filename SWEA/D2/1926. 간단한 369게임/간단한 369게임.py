T = int(input())

rule = ["3", "6", "9"]
result = []

for i in range(1, T + 1):
    arr = list(str(i))
    store = ""
    for num in arr:
        if num in rule:
            store += "-"
    if store:
        result.append(store)
    else:
        result.append(i)
print(*result)