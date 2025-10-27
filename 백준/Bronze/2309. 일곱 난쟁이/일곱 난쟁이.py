arr = []

for _ in range(9):
    arr.append(int(input()))
    
arr.sort()

for i in range(9):
    for j in range(i + 1, 9):
        copied = arr.copy()
        copied.pop(j)
        copied.pop(i)
        if sum(copied) == 100:
            for n in copied:
                print(n)
            exit()