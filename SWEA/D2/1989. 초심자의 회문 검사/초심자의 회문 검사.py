T = int(input())

for t in range(T):
    word = input()
    result = 0
    if word == word[::-1]:
        result = 1
    print(f"#{t + 1} {result}")