for t in range(10):
    N = int(input())
    word = input()
    string = input()
    result = 0
    for i in range(len(string) - len(word) + 1):
        if string[i : i + len(word)] == word:
            result += 1
    print(f"#{N} {result}")