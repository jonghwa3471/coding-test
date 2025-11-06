T = int(input())

for t in range(T):
    original = input()
    if original == original[::-1]:
        print(f"#{t + 1} 1")
    else:
        print(f"#{t + 1} 0")