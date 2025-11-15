T = int(input())

for t in range(T):
    S = list(input())
    rule = ["a", "e", "i", "o", "u"]
    result = "".join([s for s in S if s not in rule])
    print(f"#{t + 1} {result}")