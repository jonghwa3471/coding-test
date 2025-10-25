numbers = list(map(int, input().split()))

count = [0] * 7

for n in numbers:
    count[n] += 1

if 3 in count:
    num = count.index(3)
    print(10000 + num * 1000)
elif 2 in count:
    num = count.index(2)
    print(1000 + num * 100)
else:
    print(max(numbers) * 100)