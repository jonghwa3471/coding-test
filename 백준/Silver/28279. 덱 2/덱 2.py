from collections import deque
import sys

input = sys.stdin.readline

T = int(input().strip())
D = deque()
out = []

for _ in range(T):
    S = input().split()
    cmd = S[0]

    if cmd == "1":            
        D.appendleft(int(S[1]))
    elif cmd == "2":          
        D.append(int(S[1]))
    elif cmd == "3":          
        out.append(str(D.popleft() if D else -1))
    elif cmd == "4":          
        out.append(str(D.pop() if D else -1))
    elif cmd == "5":          
        out.append(str(len(D)))
    elif cmd == "6":          
        out.append('0' if D else '1')
    elif cmd == "7":          
        out.append(str(D[0]) if D else '-1')
    elif cmd == "8":          
        out.append(str(D[-1]) if D else '-1')

sys.stdout.write("\n".join(out))