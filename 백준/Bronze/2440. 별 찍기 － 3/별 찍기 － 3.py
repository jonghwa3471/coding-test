import sys

N = int(sys.stdin.readline())

for n in range(1, N + 1):
    print("*" * (N + 1 - n))